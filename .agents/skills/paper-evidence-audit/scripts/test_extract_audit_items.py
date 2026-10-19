#!/usr/bin/env python3
"""Small standard-library tests for the extraction contract and source protection."""

import csv
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
import extract_audit_items as audit


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPT = SCRIPT_DIR / "extract_audit_items.py"


class CandidateExtractionTests(unittest.TestCase):
    def test_negative_scientific_percent_and_statistical_markers(self):
        source = r"change=-2.5; shift=−3; x=+1.25e-4; y=-2E+3; rate=5%; other=4.2\%; p<.05; 95％ CI. cutoff=0.05. rate=25%."
        rows = audit.extract_text(source, "/fixture/main.tex")
        tokens = {(row["raw_token"], row["kind"]) for row in rows}
        for value in ("-2.5", "−3", "+1.25e-4", "-2E+3", ".05", "0.05"):
            self.assertIn((value, "number"), tokens)
        for value in ("5%", r"4.2\%", "95％", "25%"):
            self.assertIn((value, "percentage"), tokens)
        for value in ("p", "<", "CI"):
            self.assertIn((value, "statistical_marker"), tokens)
        self.assertTrue(all(row["status"] == "unverified" for row in rows))

    def test_repeated_values_retain_positions_and_context(self):
        rows = audit.extract_text("Baseline 12.\nProposed 12 and 12 tasks.", "/fixture/repeated.txt")
        values = [row for row in rows if row["raw_token"] == "12"]
        self.assertEqual(len(values), 3)
        self.assertEqual([row["line"] for row in values], [1, 2, 2])
        self.assertNotEqual(values[1]["column"], values[2]["column"])
        self.assertIn("Baseline", values[0]["context"])
        self.assertIn("Proposed", values[1]["context"])

    def test_citation_keys_and_numeric_key_fragments(self):
        text = r"\citep[p. 12]{Smith:2024, li-2025} and [@gao2023; -@xu_2022]. See @end2024. mail a@host.org."
        rows = audit.extract_text(text, "/fixture/citations.tex")
        keys = [row["raw_token"] for row in rows if row["kind"] == "citation_key"]
        self.assertEqual(keys, ["Smith:2024", "li-2025", "gao2023", "xu_2022", "end2024"])
        self.assertNotIn("2024", [row["raw_token"] for row in rows if row["kind"] == "number"])
        self.assertNotIn("host.org.", keys)


class FileContractTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="_audit_test_", dir=SCRIPT_DIR)
        self.root = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *(str(arg) for arg in args)],
            capture_output=True, text=True, check=False,
        )

    def test_cli_multiple_formats_and_tsv_contract(self):
        contents = {
            "paper.md": "Observed 7 tasks; p<0.05.\n",
            "note.txt": "Observed 7 other tasks.\n",
            "main.tex": r"\cite{ren2024} rate=25\%" + "\n",
            "table.csv": "group,count\nA,10\nB,20\n",
            "table.tsv": "group\tcount\nA\t30\n",
            "records.json": '{"count":40,"status":"measured"}\n',
        }
        paths = []
        for name, content in contents.items():
            path = self.root / name
            path.write_text(content, encoding="utf-8")
            paths.append(path)
        output = self.root / "reports" / "candidates.tsv"
        result = self.run_cli(*paths, "--output", output)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("unverified", result.stderr)
        with output.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream, delimiter="\t")
            self.assertEqual(tuple(reader.fieldnames), audit.FIELDS)
            rows = list(reader)
        self.assertEqual({row["source_path"] for row in rows}, {str(path.resolve()) for path in paths})
        self.assertTrue(all(row["status"] == "unverified" for row in rows))
        sevens = [row for row in rows if row["raw_token"] == "7"]
        self.assertEqual(len(sevens), 2)
        self.assertNotEqual(sevens[0]["source_path"], sevens[1]["source_path"])
        for path in paths:
            self.assertEqual(path.read_text(encoding="utf-8"), contents[path.name])

    def test_refuses_same_input_output_even_with_overwrite(self):
        source = self.root / "evidence.tsv"
        original = b"count\tvalue\nA\t15\n"
        source.write_bytes(original)
        result = self.run_cli(source, "--output", source, "--overwrite")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("input", result.stderr)
        self.assertEqual(source.read_bytes(), original)

    def test_refuses_symlink_and_hardlink_input_aliases(self):
        source = self.root / "source.tsv"
        source.write_text("value\t18\n", encoding="utf-8")
        for kind in ("symlink", "hardlink"):
            with self.subTest(kind=kind):
                alias = self.root / f"{kind}.tsv"
                if kind == "symlink":
                    alias.symlink_to(source)
                else:
                    os.link(source, alias)
                result = self.run_cli(source, "--output", alias, "--overwrite")
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(source.read_text(encoding="utf-8"), "value\t18\n")

    def test_existing_report_requires_explicit_overwrite(self):
        source = self.root / "paper.txt"
        source.write_text("12 tasks", encoding="utf-8")
        output = self.root / "report.tsv"
        output.write_text("keep this report", encoding="utf-8")
        result = self.run_cli(source, "-o", output)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(output.read_text(encoding="utf-8"), "keep this report")
        result = self.run_cli(source, "-o", output, "--overwrite")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(output.read_text(encoding="utf-8").startswith("source_path\t"))
        self.assertEqual(source.read_text(encoding="utf-8"), "12 tasks")

    def test_unsupported_and_invalid_text_fail_without_output(self):
        for name, content in (("scan.pdf", b"%PDF-1.7"), ("bad.txt", b"\xff\xfe\x00")):
            with self.subTest(name=name):
                source = self.root / name
                source.write_bytes(content)
                output = self.root / f"{name}.tsv"
                result = self.run_cli(source, "-o", output)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(output.exists())
                self.assertEqual(source.read_bytes(), content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
