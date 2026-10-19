#!/usr/bin/env python3
"""Check paper-workflow records and file freshness; never certify scientific truth."""
import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

CLAIM_FIELDS = {"claim_id", "location", "claim", "evidence_status", "evidence", "boundary", "disposition"}
ISSUE_FIELDS = {"issue_id", "location", "claim_id", "severity", "kind", "finding", "basis",
                "status", "resolution", "recheck", "closed_at"}
EVIDENCE_STATES = {"proposed", "planned", "implemented", "measured", "derived", "verified"}
ISSUE_STATES = {"open", "in-progress", "closed", "deferred", "disputed"}
STAGES = {"setup", "drafting", "reviewing", "revising", "auditing", "ready"}


def project_path(project, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError("Expected a non-empty project-relative path: " + repr(relative))
    path = (project / relative).resolve()
    if not path.is_relative_to(project):
        raise ValueError("Path leaves the project: " + relative)
    return path


def read_json(path):
    result = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(result, dict):
        raise ValueError(str(path) + " must contain a JSON object")
    return result


def read_table(path, fields):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if not fields.issubset(set(reader.fieldnames or [])):
            raise ValueError(str(path) + " is missing required columns")
        rows = []
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(str(path) + " contains a malformed TSV row")
            if any(value.strip() for value in row.values()):
                rows.append(row)
        return rows


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def required_inputs(config, state):
    paths = ["research/PROJECT.json", config["claims_file"], config["issues_file"], config["sources_file"]]
    paths.extend(config["manuscript_paths"])
    paths.extend(config.get("evidence_files", []))
    for check in state.get("checks", {}).values():
        if isinstance(check, dict):
            paths.extend(check.get("artifacts", []))
    if not all(isinstance(path, str) and path for path in paths):
        raise ValueError("Input and artifact paths must be non-empty strings")
    state_path = config["state_file"]
    if state_path in paths:
        raise ValueError("The state file cannot include its own hash")
    return sorted(set(paths))


def load_project(project):
    config = read_json(project / "research/PROJECT.json")
    required = {"schema_version", "state_file", "manuscript_paths", "claims_file",
                "issues_file", "sources_file", "required_checks"}
    if not required.issubset(config):
        raise ValueError("PROJECT.json is missing required fields")
    if config["schema_version"] != 1:
        raise ValueError("Unsupported project schema version")
    if not isinstance(config["manuscript_paths"], list) or not config["manuscript_paths"]:
        raise ValueError("manuscript_paths must be a non-empty list")
    if not isinstance(config["required_checks"], list) or not set(
            ["claims", "numbers", "citations", "manuscript_boundary"]).issubset(config["required_checks"]):
        raise ValueError("required_checks must include claims, numbers, citations and manuscript_boundary")
    if not isinstance(config.get("evidence_files", []), list):
        raise ValueError("evidence_files must be a list")
    state = read_json(project_path(project, config["state_file"]))
    if state.get("schema_version") != 1 or state.get("stage") not in STAGES:
        raise ValueError("Invalid state schema or stage")
    if not isinstance(state.get("submission_requested"), bool):
        raise ValueError("submission_requested must be a boolean")
    if not isinstance(state.get("checks"), dict) or not isinstance(state.get("checked_artifact_sha256"), dict):
        raise ValueError("checks and checked_artifact_sha256 must be objects")
    if not isinstance(state.get("remaining_blockers"), list):
        raise ValueError("remaining_blockers must be a list")
    return config, state


def evaluate(project, submission=False):
    project = Path(project).resolve()
    issues = []
    try:
        config, state = load_project(project)
        if not submission and not state["submission_requested"]:
            return {"status": "NOT_REQUESTED", "issues": [],
                    "scientific_validity": "not_assessed_by_script",
                    "message": "Submission gate not requested; no readiness assessment performed."}
        claims = read_table(project_path(project, config["claims_file"]), CLAIM_FIELDS)
        records = read_table(project_path(project, config["issues_file"]), ISSUE_FIELDS)
        if not claims:
            issues.append("Claim ledger is empty.")
        ids = set()
        for claim in claims:
            cid = claim["claim_id"].strip()
            if not cid or cid in ids:
                issues.append("Missing or duplicate claim ID: " + repr(cid))
            ids.add(cid)
            if claim["evidence_status"] not in EVIDENCE_STATES:
                issues.append(cid + ": invalid evidence status.")
            if claim["disposition"] not in {"active", "narrowed", "withdrawn"}:
                issues.append(cid + ": invalid disposition.")
            if not claim["location"].strip() or not claim["claim"].strip():
                issues.append(cid + ": claim text and location are required.")
            if claim["disposition"] != "withdrawn" and claim["evidence_status"] in {
                    "implemented", "measured", "derived", "verified"} and not claim["evidence"].strip():
                issues.append(cid + ": evidence reference is missing.")
        issue_ids = set()
        for record in records:
            iid = record["issue_id"].strip()
            if not iid or iid in issue_ids:
                issues.append("Missing or duplicate issue ID: " + repr(iid))
            issue_ids.add(iid)
            if record["status"] not in ISSUE_STATES:
                issues.append(iid + ": invalid issue status.")
            if record["severity"] not in {"blocking", "major", "minor", "editorial"}:
                issues.append(iid + ": invalid severity.")
            if record["kind"] not in {"confirmed", "suspected", "missing-evidence", "preference"}:
                issues.append(iid + ": invalid issue kind.")
            if record["claim_id"] and record["claim_id"] not in ids:
                issues.append(iid + ": unknown claim ID.")
            if not record["location"].strip() or not record["finding"].strip() or not record["basis"].strip():
                issues.append(iid + ": location, finding and basis are required.")
            if record["status"] == "closed":
                if not all(record[key].strip() for key in ("resolution", "recheck", "closed_at")):
                    issues.append(iid + ": closed issue lacks resolution, recheck or date.")
            elif record["severity"] in {"blocking", "major"}:
                issues.append(iid + ": unresolved material issue (" + record["status"] + ").")
        if state["remaining_blockers"]:
            issues.append("State contains remaining blockers.")
        for name in config["required_checks"]:
            check = state["checks"].get(name, {})
            if not isinstance(check, dict):
                issues.append(name + ": invalid check record.")
                continue
            status = check.get("status")
            if status not in {"pass", "not_applicable"}:
                issues.append(name + ": check is not complete.")
            if status == "not_applicable" and name not in {"numbers", "citations"}:
                issues.append(name + ": this check cannot be not_applicable.")
            if not isinstance(check.get("basis"), str) or not check["basis"].strip():
                issues.append(name + ": check basis is missing.")
            artifacts = check.get("artifacts")
            if not isinstance(artifacts, list) or not artifacts:
                issues.append(name + ": a check report or audited record is required.")
        snapshots = state["checked_artifact_sha256"]
        paths = set(required_inputs(config, state)) | set(snapshots)
        for relative in sorted(paths):
            path = project_path(project, relative)
            if not path.is_file():
                issues.append(relative + ": required checked file is missing.")
                continue
            expected = snapshots.get(relative)
            if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
                issues.append(relative + ": checked SHA-256 is missing or invalid.")
            elif sha256(path) != expected:
                issues.append(relative + ": changed since the recorded checks.")
    except (OSError, ValueError, KeyError, TypeError, csv.Error) as exc:
        issues.append(str(exc))
    return {"status": "BLOCKED" if issues else "RECORDED_CHECKS_CURRENT",
            "issues": issues, "scientific_validity": "not_assessed_by_script",
            "message": "Checks records, unresolved material issues and file freshness only."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check")
    check.add_argument("--project", type=Path, default=Path("."))
    check.add_argument("--submission", action="store_true")
    snap = sub.add_parser("snapshot", help="Print file hashes; does not approve checks or edit state")
    snap.add_argument("--project", type=Path, default=Path("."))
    snap.add_argument("--files", nargs="*", default=[])
    args = parser.parse_args()
    if args.command == "check":
        result = evaluate(args.project, args.submission)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 2 if result["status"] == "BLOCKED" else 0
    try:
        project = args.project.resolve()
        config, state = load_project(project)
        paths = sorted(set(required_inputs(config, state) + args.files))
        if config["state_file"] in paths:
            raise ValueError("Cannot snapshot the state file into itself")
        result = {path: sha256(project_path(project, path)) for path in paths}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
