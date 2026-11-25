#!/usr/bin/env python3
"""Find candidate metadata in one Crossref journal. Use public search terms."""

import argparse
from datetime import datetime, timezone
from http.client import HTTPException
import json
import re
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def normalize_issn(value):
    digits = value.strip().upper().replace("-", "")
    if re.fullmatch(r"[0-9]{7}[0-9X]", digits):
        check = (-sum(int(d) * w for d, w in zip(digits[:7], range(8, 1, -1)))) % 11
        if digits[-1] == ("X" if check == 10 else str(check)):
            return digits[:4] + "-" + digits[4:]
    raise argparse.ArgumentTypeError("expected an ISSN with a valid check digit")


def query_url(issn, query, rows):
    params = urlencode({
        "query.bibliographic": query,
        "filter": "type:journal-article",
        "rows": rows,
        "select": "DOI,title,container-title,published,type,ISSN",
    })
    return f"https://api.crossref.org/journals/{issn}/works?{params}"


def candidates(payload):
    if not isinstance(payload, dict) or payload.get("status") != "ok":
        raise ValueError("unexpected Crossref response")
    message = payload.get("message")
    if not isinstance(message, dict) or not isinstance(message.get("items"), list):
        raise ValueError("Crossref response has no items list")
    found = {}
    for item in message["items"]:
        if not isinstance(item, dict) or not isinstance(item.get("DOI"), str):
            raise ValueError("Crossref record has no DOI")
        doi = item["DOI"].strip().lower()
        if not doi:
            raise ValueError("Crossref record has an empty DOI")
        if doi in found:
            continue
        dates = (item.get("published") or {}).get("date-parts") or []
        found[doi] = {
            "doi": doi,
            "title": next(iter(item.get("title") or []), None),
            "journal": next(iter(item.get("container-title") or []), None),
            "issns": item.get("ISSN") or [],
            "year": dates[0][0] if dates and dates[0] else None,
            "crossref_type": item.get("type"),
            "url": f"https://doi.org/{doi}",
        }
    return list(found.values())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issn", required=True, type=normalize_issn,
                        help="print or online ISSN verified against the target journal")
    parser.add_argument("--query", required=True, help="public topic or method keywords")
    parser.add_argument("--rows", type=int, default=10, help="metadata search window (1 to 100)")
    args = parser.parse_args(argv)
    query = args.query.strip()
    if not query or not 1 <= args.rows <= 100:
        parser.error("supply a nonempty query and --rows between 1 and 100")
    url = query_url(args.issn, query, args.rows)
    report = {"source": "Crossref", "issn": args.issn, "query": query, "rows": args.rows,
              "url": url, "checked_at": datetime.now(timezone.utc).isoformat()}
    request = Request(url, headers={"User-Agent": "paper-review-writing-skill/1.0",
                                    "Accept": "application/json"})
    try:
        with urlopen(request, timeout=20) as response:
            records = candidates(json.load(response))
    except (OSError, HTTPException, ValueError) as exc:
        print(json.dumps({**report, "status": "lookup_failed", "error": str(exc)},
                         ensure_ascii=False), file=sys.stderr)
        return 1
    report.update(status="metadata_candidates" if records else "no_candidates", candidates=records)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
