#!/usr/bin/env python3
"""Optional local Stop notification. Always exits zero; never asks Codex to continue."""
import json
import sys
from pathlib import Path
from paper_gate import evaluate, load_project


def main():
    result = {}
    try:
        raw = sys.stdin.read(1_000_001)
        if len(raw) > 1_000_000:
            raise ValueError("Hook input exceeds the supported size")
        payload = json.loads(raw or "{}")
        if not isinstance(payload, dict):
            raise ValueError("Hook input must be a JSON object")
        project = Path(__file__).resolve().parents[1]
        _, state = load_project(project)
        if (state["submission_requested"] and state["stage"] in {"auditing", "ready"}
                and not payload.get("stop_hook_active", False)):
            report = evaluate(project, submission=True)
            if report["status"] == "BLOCKED":
                detail = "; ".join(report["issues"][:3])
                result = {"systemMessage": "Paper workflow records need attention: " + detail
                          + ". Run tools/paper_gate.py check --project . --submission for the full report."}
    except Exception as exc:
        result = {"systemMessage": "Optional paper check could not run: " + str(exc)}
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
