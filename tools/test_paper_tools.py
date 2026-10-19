#!/usr/bin/env python3
"""Behavior checks for installation, record gates and the optional Stop wrapper."""
import contextlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import paper_gate
import install_project


class GateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.project = Path(self.tmp.name)
        (self.project / "research").mkdir()
        (self.project / "manuscript").mkdir()
        (self.project / "manuscript/main.md").write_text("Observed 8 completions in 10 tasks.\n")
        (self.project / "research/check.md").write_text("Fictional fixture: checked this example only.\n")
        (self.project / "research/claims.tsv").write_text(
            "claim_id\tlocation\tclaim\tevidence_status\tevidence\tboundary\tdisposition\n"
            "C1\tmanuscript/main.md\t8 of 10\tmeasured\tfixture record\tone run\tactive\n")
        (self.project / "research/issues.tsv").write_text(
            "issue_id\tlocation\tclaim_id\tseverity\tkind\tfinding\tbasis\tstatus\tresolution\trecheck\tclosed_at\n")
        (self.project / "research/sources.tsv").write_text("source_id\tpath_or_url\n")
        self.config = {
            "schema_version": 1, "state_file": "research/state.json",
            "manuscript_paths": ["manuscript/main.md"], "claims_file": "research/claims.tsv",
            "issues_file": "research/issues.tsv", "sources_file": "research/sources.tsv",
            "required_checks": ["claims", "numbers", "citations", "manuscript_boundary"]}
        (self.project / "research/PROJECT.json").write_text(json.dumps(self.config))
        self.state = {
            "schema_version": 1, "stage": "auditing", "submission_requested": True,
            "checks": {name: {"status": "pass", "basis": "Fictional fixture check",
                             "artifacts": ["research/check.md"]}
                       for name in self.config["required_checks"]},
            "checked_artifact_sha256": {}, "remaining_blockers": []}
        self.snapshot()

    def save(self):
        (self.project / "research/state.json").write_text(json.dumps(self.state))

    def snapshot(self):
        self.state["checked_artifact_sha256"] = {
            path: paper_gate.sha256(self.project / path)
            for path in paper_gate.required_inputs(self.config, self.state)}
        self.save()

    def test_complete_records_do_not_claim_scientific_validity(self):
        result = paper_gate.evaluate(self.project, True)
        self.assertEqual(result["status"], "RECORDED_CHECKS_CURRENT")
        self.assertEqual(result["scientific_validity"], "not_assessed_by_script")

    def test_changed_manuscript_invalidates_recorded_check(self):
        (self.project / "manuscript/main.md").write_text("Observed 9 completions in 10 tasks.\n")
        result = paper_gate.evaluate(self.project, True)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertTrue(any("changed since" in issue for issue in result["issues"]))

    def test_major_deferred_issue_blocks_even_with_fresh_hashes(self):
        path = self.project / "research/issues.tsv"
        path.write_text(path.read_text() +
                        "R1\tmanuscript/main.md\tC1\tmajor\tmissing-evidence\tControl absent\tRecords inspected\tdeferred\t\t\t\n")
        self.snapshot()
        result = paper_gate.evaluate(self.project, True)
        self.assertTrue(any("unresolved material issue" in issue for issue in result["issues"]))

    def test_closed_issue_without_recheck_blocks(self):
        path = self.project / "research/issues.tsv"
        path.write_text(path.read_text() +
                        "R1\tmanuscript/main.md\tC1\tmajor\tconfirmed\tWrong value\tRaw record\tclosed\tCorrected\t\t2026-10-19\n")
        self.snapshot()
        result = paper_gate.evaluate(self.project, True)
        self.assertTrue(any("closed issue lacks" in issue for issue in result["issues"]))

    def test_claim_checks_cannot_be_skipped_with_not_applicable(self):
        self.state["checks"]["claims"]["status"] = "not_applicable"
        self.save()
        result = paper_gate.evaluate(self.project, True)
        self.assertTrue(any("cannot be not_applicable" in issue for issue in result["issues"]))

    def test_no_submission_request_does_not_invent_readiness(self):
        self.state["submission_requested"] = False
        self.save()
        self.assertEqual(paper_gate.evaluate(self.project)["status"], "NOT_REQUESTED")

    def test_paths_cannot_escape_project(self):
        self.state["checked_artifact_sha256"]["../outside"] = "0" * 64
        self.save()
        result = paper_gate.evaluate(self.project, True)
        self.assertTrue(any("leaves the project" in issue for issue in result["issues"]))

    def test_active_stop_hook_reports_block_without_requesting_continuation(self):
        hook_tools = self.project / "tools"
        hook_tools.mkdir()
        for name in ("paper_gate.py", "manuscript_stop_hook.py"):
            (hook_tools / name).write_bytes((TOOLS / name).read_bytes())
        (self.project / "manuscript/main.md").write_text("Changed after review.\n")
        command = [sys.executable, str(hook_tools / "manuscript_stop_hook.py")]
        run = subprocess.run(command, input="{}", capture_output=True, text=True)
        self.assertEqual(run.returncode, 0)
        report = json.loads(run.stdout)
        self.assertEqual(set(report), {"systemMessage"})
        self.assertIn("changed since", report["systemMessage"])
        repeated = subprocess.run(command, input='{"stop_hook_active": true}',
                                  capture_output=True, text=True)
        self.assertEqual(repeated.returncode, 0)
        self.assertEqual(json.loads(repeated.stdout), {})


class InstallationTests(unittest.TestCase):
    def test_existing_rules_and_records_preserved_and_install_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            (target / "AGENTS.md").write_text("# Existing engineering rules\nUse the existing test command.\n")
            (target / "research").mkdir()
            (target / "research/state.json").write_text('{"my_existing_state": true}\n')
            actions, conflicts, _, agents, original, merged = install_project.plan_install(ROOT, target)
            self.assertFalse(conflicts)
            self.assertTrue(merged.startswith(original.rstrip()))
            self.assertNotIn(target / "research/state.json", [dest for _, dest in actions])
            for source, dest in actions:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(source.read_bytes())
            agents.write_text(merged)
            again, conflicts, _, _, before, after = install_project.plan_install(ROOT, target)
            self.assertEqual(again, [])
            self.assertEqual(conflicts, [])
            self.assertEqual(before, after)
            self.assertEqual(json.loads((target / "research/state.json").read_text()), {"my_existing_state": True})

    def test_conflict_is_found_before_writing_any_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            (target / "ACADEMIC_WRITING.md").write_text("Author-specific rules.\n")
            run = subprocess.run([sys.executable, str(TOOLS / "install_project.py"),
                                  "--project", str(target)], capture_output=True, text=True)
            self.assertEqual(run.returncode, 2)
            self.assertTrue(json.loads(run.stdout)["conflicts"])
            self.assertEqual(sorted(p.name for p in target.iterdir()), ["ACADEMIC_WRITING.md"])


class HookTests(unittest.TestCase):
    def test_starter_hook_exits_zero_without_block_or_continuation(self):
        run = subprocess.run([sys.executable, str(TOOLS / "manuscript_stop_hook.py")],
                             input="{}", capture_output=True, text=True)
        self.assertEqual(run.returncode, 0)
        self.assertEqual(json.loads(run.stdout), {})

    def test_malformed_hook_input_is_notification_only(self):
        run = subprocess.run([sys.executable, str(TOOLS / "manuscript_stop_hook.py")],
                             input="{", capture_output=True, text=True)
        self.assertEqual(run.returncode, 0)
        result = json.loads(run.stdout)
        self.assertIn("systemMessage", result)
        self.assertNotIn("decision", result)


if __name__ == "__main__":
    unittest.main()
