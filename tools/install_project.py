#!/usr/bin/env python3
"""Install this starter into a project, merging its AGENTS block and preserving user files."""
import argparse
import json
import shutil
import sys
from pathlib import Path

START = "<!-- BEGIN CODEX PAPER WORKFLOW -->"
END = "<!-- END CODEX PAPER WORKFLOW -->"
SKILLS = ("paper-harness", "paper-positioning", "paper-draft", "paper-voice",
          "paper-rewrite", "paper-redteam", "paper-evidence-audit", "paper-revision")
DOCS = ("ACADEMIC_WRITING.md", "RESEARCH_HARNESS.md", "PROMPTS.md", "METHODS_AND_SOURCES.md", "SKILL_GUIDE.md")


def sources(source, examples=False):
    items = []
    for name in SKILLS:
        folder = source / ".agents/skills" / name
        if not (folder / "SKILL.md").is_file():
            raise ValueError("Incomplete starter; missing " + str(folder / "SKILL.md"))
        items.extend(path for path in folder.rglob("*") if path.is_file() and "__pycache__" not in path.parts)
    for name in DOCS:
        items.append(source / name)
    for name in ("tools", "prompts", "research", "optional"):
        folder = source / name
        if folder.exists():
            items.extend(path for path in folder.rglob("*") if path.is_file() and "__pycache__" not in path.parts)
    if examples and (source / "examples").exists():
        items.extend(path for path in (source / "examples").rglob("*") if path.is_file())
    for path in items:
        if not path.is_file():
            raise ValueError("Incomplete starter; missing " + str(path))
    return sorted(set(items))


def plan_install(source, destination, examples=False):
    if not destination.is_dir():
        raise ValueError("Target project must already exist")
    if source == destination:
        raise ValueError("Source and target are the same project")
    actions, conflicts, preserved = [], [], []
    for src in sources(source, examples):
        rel = src.relative_to(source)
        dest = destination / rel
        if dest.is_symlink() or not dest.resolve().is_relative_to(destination):
            conflicts.append(str(rel) + ": symlink or path outside project")
            continue
        if dest.exists():
            if not dest.is_file():
                conflicts.append(str(rel) + ": destination is not a file")
            elif dest.read_bytes() == src.read_bytes():
                preserved.append(str(rel))
            elif rel.parts[0] == "research":
                preserved.append(str(rel) + " (existing project record)")
            else:
                conflicts.append(str(rel) + ": different existing file; merge explicitly")
        else:
            actions.append((src, dest))
    agents = destination / "AGENTS.md"
    block = (source / "AGENTS.md").read_text(encoding="utf-8").strip()
    original = agents.read_text(encoding="utf-8") if agents.is_file() else ""
    if agents.is_symlink() or not agents.resolve().is_relative_to(destination):
        conflicts.append("AGENTS.md: symlink or path outside project")
    elif agents.exists() and not agents.is_file():
        conflicts.append("AGENTS.md is not a file")
    if START in original or END in original:
        if original.count(START) != 1 or original.count(END) != 1:
            conflicts.append("AGENTS.md: malformed or duplicate workflow markers")
            merged = original
        else:
            begin = original.index(START)
            end = original.index(END)
            if end < begin:
                conflicts.append("AGENTS.md: reversed workflow markers")
                merged = original
            else:
                end += len(END)
                existing = original[begin:end].strip()
                if existing != block:
                    conflicts.append("AGENTS.md: existing workflow block differs; merge explicitly")
                merged = original
    else:
        merged = original.rstrip() + ("\n\n" if original.strip() else "") + block + "\n"
    return actions, conflicts, preserved, agents, original, merged


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--include-examples", action="store_true")
    args = parser.parse_args()
    try:
        src, dst = args.source.resolve(), args.project.resolve()
        actions, conflicts, preserved, agents, original, merged = plan_install(src, dst, args.include_examples)
        report = {"mode": "preview" if args.dry_run else "install",
                  "copy": [str(d.relative_to(dst)) for _, d in actions],
                  "merge_agents": merged != original, "preserved": preserved, "conflicts": conflicts}
        if conflicts or args.dry_run:
            print(json.dumps(report, ensure_ascii=False, indent=2))
            return 2 if conflicts else 0
        for source, target in actions:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        if merged != original:
            agents.write_text(merged, encoding="utf-8")
        report["status"] = "installed"
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
