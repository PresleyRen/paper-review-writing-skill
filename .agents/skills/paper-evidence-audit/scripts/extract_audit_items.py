#!/usr/bin/env python3
"""Index candidate numbers, statistical markers, and citation keys in local text.

No candidate is verified by this script. All output statuses are "unverified".
This is lexical, single-line extraction, not a PDF reader or a TeX/CSV/JSON parser.
It uses only the Python standard library and never changes source files.
"""

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Iterable


ALLOWED_SUFFIXES = {".md", ".txt", ".tex", ".csv", ".tsv", ".json"}
FIELDS = ("source_path", "line", "column", "context", "raw_token", "kind", "status")

# Keep the source spelling. No float conversion, unit conversion, or calculation.
NUMBER_RE = re.compile(
    r"(?<![\w.])"
    r"[+\-\u2212]?"
    r"(?:\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?|\.\d+)"
    r"(?:[eE][+\-\u2212]?\d+)?"
    r"(?:[ \t]*\\?[%\uff05])?"
    r"(?!\d|\.\d)"
)

# Common single-line LaTeX cite commands; custom macros can be missed.
CITE_COMMAND_RE = re.compile(
    r"\\(?:[Cc]ite[a-zA-Z]*|[Pp]arencite[a-zA-Z]*|[Tt]extcite[a-zA-Z]*"
    r"|[Aa]utocite[a-zA-Z]*|[Nn]ocite|[Ff]ootcite[a-zA-Z]*|[Ss]martcite)"
    r"\*?(?:[ \t]*\[[^\]\r\n]*\])*[ \t]*\{(?P<keys>[^{}\r\n]+)\}"
)
PANDOC_CITE_RE = re.compile(
    r"(?<![\w@.])@(?P<key>[A-Za-z_](?:[\w:./+\-]*[\w/+\-])?)"
)
STAT_RE = re.compile(
    r"\\(?:pm|leq?|geq?|approx|neq|sigma|mu|chi|Delta|delta|beta|alpha|rho|tau|eta)\b"
    r"|[±≤≥≈≠σμχΔδβαρτη<>=]"
    r"|(?<![\w\\])(?:p|q|n|N|t|z|r|d|F|df|CI|SD|SE|SEM|IQR|OR|RR|HR"
    r"|AUC|MSE|RMSE|MAE|F1|R2|R²)(?!\w)"
)


def _overlaps(start: int, end: int, spans: list[tuple[int, int]]) -> bool:
    return any(start < other_end and end > other_start for other_start, other_end in spans)


def _context(line: str, start: int, end: int, width: int) -> str:
    width = max(width, end - start)
    left = max(0, start - (width - (end - start)) // 2)
    right = min(len(line), left + width)
    left = max(0, right - width)
    return line[left:right]


def extract_text(text: str, source_path: str, context_chars: int = 240) -> list[dict]:
    """Return every candidate occurrence with one-based line and column numbers."""
    if context_chars < 1:
        raise ValueError("context_chars must be positive")
    rows = []
    for line_number, line in enumerate(text.splitlines(), 1):
        candidates: list[tuple[int, int, str]] = []
        citation_spans: list[tuple[int, int]] = []
        for command in CITE_COMMAND_RE.finditer(line):
            base = command.start("keys")
            for key in re.finditer(r"[^,\s]+", command.group("keys")):
                if key.group() == "*":
                    continue
                start, end = base + key.start(), base + key.end()
                candidates.append((start, end, "citation_key"))
                citation_spans.append((start, end))
        for citation in PANDOC_CITE_RE.finditer(line):
            start, end = citation.span("key")
            if not _overlaps(start, end, citation_spans):
                candidates.append((start, end, "citation_key"))
                citation_spans.append((start, end))
        for number in NUMBER_RE.finditer(line):
            start, end = number.span()
            if not _overlaps(start, end, citation_spans):
                kind = "percentage" if number.group().endswith(("%", "％")) else "number"
                candidates.append((start, end, kind))
        for marker in STAT_RE.finditer(line):
            start, end = marker.span()
            if not _overlaps(start, end, citation_spans):
                candidates.append((start, end, "statistical_marker"))
        # Do not deduplicate by token value: two equal values can make different claims.
        for start, end, kind in sorted(candidates):
            rows.append({
                "source_path": source_path,
                "line": line_number,
                "column": start + 1,
                "context": _context(line, start, end, context_chars),
                "raw_token": line[start:end],
                "kind": kind,
                "status": "unverified",
            })
    return rows


def load_inputs(paths: Iterable[str], context_chars: int) -> tuple[list[Path], list[dict]]:
    sources, rows = [], []
    for item in paths:
        source = Path(item).expanduser().resolve(strict=True)
        if not source.is_file():
            raise ValueError(f"Input is not a regular file: {source}")
        if source.suffix.lower() not in ALLOWED_SUFFIXES:
            raise ValueError(f"Unsupported input suffix: {source.suffix}; use local UTF-8 text")
        text = source.read_text(encoding="utf-8-sig")
        if "\x00" in text:
            raise ValueError(f"Input contains NUL bytes and is not supported text: {source}")
        sources.append(source)
        rows.extend(extract_text(text, str(source), context_chars))
    return sources, rows


def validate_destination(output: Path, sources: list[Path], overwrite: bool) -> None:
    """Refuse an input path, symlink, hardlink alias, or unrequested report overwrite."""
    resolved_output = output.resolve()
    for source in sources:
        if resolved_output == source.resolve():
            raise ValueError(f"Output would overwrite an input file: {source}")
        if output.exists() and output.samefile(source):
            raise ValueError(f"Output is a hardlink alias of an input file: {source}")
    if output.is_symlink():
        raise ValueError(f"Refusing a symlink output: {output}")
    if output.exists() and not output.is_file():
        raise ValueError(f"Output is not a regular file: {output}")
    if output.exists() and not overwrite:
        raise ValueError(f"Output already exists; choose a new path or use --overwrite: {output}")


def write_tsv(
    rows: list[dict], output: Path, sources: list[Path], overwrite: bool = False
) -> None:
    validate_destination(output, sources, overwrite)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="", dir=output.parent,
            prefix=".audit-candidates-", suffix=".tsv", delete=False
        ) as stream:
            temporary = Path(stream.name)
            writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        validate_destination(output, sources, overwrite)
        if overwrite:
            os.replace(temporary, output)
        else:
            # Atomic no-clobber publication. The temporary file is on the same filesystem.
            os.link(temporary, output)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="Local UTF-8 .md/.txt/.tex/.csv/.tsv/.json files")
    parser.add_argument("-o", "--output", required=True, help="Destination TSV, separate from all inputs")
    parser.add_argument("--context-chars", type=int, default=240, help="Single-line context window (default: 240)")
    parser.add_argument("--overwrite", action="store_true", help="Replace an existing report, never an input")
    args = parser.parse_args(argv)
    if args.context_chars < 1:
        parser.error("--context-chars must be positive")
    try:
        sources, rows = load_inputs(args.inputs, args.context_chars)
        output = Path(args.output).expanduser().absolute()
        write_tsv(rows, output, sources, args.overwrite)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))
    print(
        f"Wrote {len(rows)} unverified candidates from {len(sources)} file(s) to {output}. "
        "Extraction does not verify numbers, citations, or scientific claims.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
