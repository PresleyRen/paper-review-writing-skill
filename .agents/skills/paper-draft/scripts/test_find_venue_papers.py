import argparse
import contextlib
import io
import json
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlsplit

import find_venue_papers as search


class VenueLookupTests(unittest.TestCase):
    def test_issn_and_keyword_scope(self):
        issn = search.normalize_issn("09507051")
        url = urlsplit(search.query_url(issn, "retrieval & tools", 7))
        self.assertEqual(url.path, "/journals/0950-7051/works")
        self.assertEqual(parse_qs(url.query)["query.bibliographic"], ["retrieval & tools"])
        with self.assertRaises(argparse.ArgumentTypeError):
            search.normalize_issn("0950-7052")

    def test_doi_deduplication_preserves_first_record(self):
        first = {"DOI": "10.9999/Example", "title": ["First title"],
                 "container-title": ["Journal"], "published": {"date-parts": [[2024]]}}
        items = [first, {"DOI": "10.9999/example", "title": ["Duplicate"]}]
        records = search.candidates({"status": "ok", "message": {"items": items}})
        self.assertEqual(len(records), 1)
        self.assertEqual((records[0]["doi"], records[0]["title"], records[0]["year"]),
                         ("10.9999/example", "First title", 2024))

    def test_empty_page_is_distinct_from_failure(self):
        args = ["--issn", "0950-7051", "--query", "retrieval"]
        for body, code, status in [
            (b'{"status":"ok","message":{"items":[]}}', 0, "no_candidates"),
            (b'{}', 1, "lookup_failed"),
            (b'<html>Service unavailable</html>', 1, "lookup_failed"),
        ]:
            with self.subTest(body=body), patch.object(search, "urlopen", return_value=io.BytesIO(body)):
                out, err = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                    self.assertEqual(search.main(args), code)
                report = json.loads((err if code else out).getvalue())
                self.assertEqual(report["status"], status)
                self.assertIn("url", report)

    def test_http_error_retains_request_provenance(self):
        error = HTTPError("https://api.crossref.org", 429, "Too Many Requests", {}, None)
        err = io.StringIO()
        with patch.object(search, "urlopen", side_effect=error), contextlib.redirect_stderr(err):
            code = search.main(["--issn", "0950-7051", "--query", "retrieval"])
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(err.getvalue())["status"], "lookup_failed")


if __name__ == "__main__":
    unittest.main()
