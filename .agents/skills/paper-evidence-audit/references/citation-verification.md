# Citation verification: write-time admission and submission audit

Updated 2026-11-26. This is an original local integration of research methods, not a copy or installation of third-party code. The evidence audit owns citation decisions; the draft and harness route here. Use the existing project sources/claims/issues/state records and extraction tooling rather than creating a second evidence system.

## 1. Trigger and scope

| Mode | Trigger | Required result |
| --- | --- | --- |
| admission | Before inserting a new or substantively changed external claim/citation into any draft | Verify identity, applicable metadata, publication status and support of that exact claim; retain only supported wording. |
| local | User requests a citation check or a revision changes a citation, claim, source version or interpretation | Recheck affected occurrences and dependent claims. |
| submission | User requests a full pre-submission review | Inventory all citation occurrences and bibliography keys in the actual manuscript, check all used references and each attributed claim, resolve material issues and record the checked versions. |
| language only | Grammar, style or translation without a change in meaning or references | Preserve citation bindings; recheck only if meaning, attribution or scope changes. Do not launch a network search automatically. |

Admission is part of drafting, not an instruction to postpone the verification until the paper is complete. Reuse existing evidence only when the source version, checked passage, claim scope and relevant publication status remain appropriate. If the requested task prohibits external searches, work from supplied material and report unverified points rather than treating memory as evidence.

## 2. Check local structure

Use the existing extract_audit_items.py as a locator, not as a complete bibliography parser. Inspect the actual Markdown, LaTeX, Typst, Word or PDF, using the host's suitable tools. For a complete audit build a manifest of every cited key and occurrence, including grouped citations, tables, figures, captions, footnotes, appendix and supplementary material in scope. Resolve keys to their bibliography entries; check duplicates, collisions, missing keys, placeholders and identifier syntax. Uncited entries in a shared library are advisory unless the target venue requires removal. Record format/coverage limitations explicitly. A unique key is not evidence of a unique or real work.

## 3. Resolve identity and compare fields

Query DOI registration (Crossref or DataCite) and the authoritative publisher/official proceedings, or an appropriate source such as ACL Anthology, DBLP, OpenReview, arXiv, PubMed or a thesis repository. Use title + first author and year as a fallback, including works without DOI. Open the actual returned record; search results alone are discovery. Prefer a canonical record plus a second appropriate source when obtainable; distinguish mirrored metadata from independently sourced information. Record actual sources tried, access dates, conflicts and errors.

Compare title, ordered authors, venue, year (online vs issue publication), DOI or persistent identifier, article type, version, volume, issue, pages or article number, as applicable. Resolve the identifier to the intended work, not just an HTTP success. An absent DOI, 404 from one registry, 429, timeout or index miss is not sufficient to declare fabrication. Do not invent fields for early-access items or unavailable records. Preserve preprint vs published distinctions and check whether the version contains the cited result. Label each material field mismatch and its proposed correction with evidence. Generate BibTeX or reference-format patches only from checked records; do not silently change shared libraries or citation keys.

Check relevant publisher notices, corrections, expressions of concern and retractions (e.g. publisher/Crossmark and Crossref Retraction Watch data if accessible). Record where and when status was checked; no notice found is not a guarantee of no retraction. If an affected work is relevant as a historical or retracted object of discussion, explicitly identify that status rather than cite it as unqualified evidence. Unknown status is an unresolved check, not a clean result.

## 4. Verify claim-to-source support per occurrence

For each occurrence split the sentence into its material attributable claims. Record key, manuscript file and locator, exact claim, source URL/version, inspected section/page/table/figure/theorem and short evidence excerpt or accurate evidence summary. For each pairing decide supported, contradicted, partial, or unavailable/unclear. Separate existence, metadata and semantic decisions; do not let one substitute for another.

Read the primary work where the claim requires it. Check the task, population, metric, comparator, dataset/split, model, experimental condition, effect size, uncertainty, negation, and scope. Distinguish authors' speculation from measured results and survey paraphrase from original evidence. For LLM/Agent papers do not confuse intent accuracy with tool selection or end-to-end success; a retrieval Recall@k result does not establish generation accuracy. When several sources are grouped, show which source supports each clause rather than assume all do. An abstract can support a claim explicitly established there; detailed numbers, limitations and causality normally require the relevant full-text location. Do not quote a search snippet as a paper passage or fabricate a page number.

A proposer supplies candidate sources and evidence; an independent skeptic checks the precise pairing and tries to disconfirm it. For major, quantitative, disputed, or submission claims use a fresh isolated reviewer when the host actually supports it. Send the claim and source identity, not the proposer's verdict or desired outcome. Record actual reviewer/tool, model if known, context isolation and whether source access occurred. When isolation is unavailable, perform a separate sequential check and disclose the limitation; never claim double-blind or cross-model verification. For metadata disagreement independently reconstruct the authoritative record before comparing with local bibliography when isolation is possible. Recheck contradictory conclusions against original sources.

## 5. Decisions and repairs

| Axis | Allowed values |
| --- | --- |
| identity | confirmed / mismatch / not_found_after_search / unavailable |
| metadata | matched / correction_needed / conflicting / unavailable |
| publication_status | checked_no_notice_found / corrected / concern / retracted / unavailable |
| support | supported / partial / contradicted / unavailable / unclear |
| action | keep / fix_metadata / narrow_claim / replace_source / remove_attribution / needs_review |

Use the existing audit finding statuses from audit_protocol.md; these axis fields are supplemental, not new values for research/claims.tsv. A supported claim requires the correct source/version and inspected relevant evidence; a correction/concern needs explicit handling. Never equate missing access with a fake citation. A non-existent or misattributed work must not be treated as evidence. For partial support, narrow the sentence only to what the source establishes; for unsupported claims find a suitable checked primary source or omit/flag the claim. Do not replace a source with a merely topical candidate. Review-only tasks propose fixes; authorized draft/revision tasks may apply evidenced repairs and recheck affected occurrences. Keep author approval for material changes of scientific claims or bibliography deletions outside the requested scope. Preserve rejected source/claim pairings and reasons to avoid re-suggesting them.

## 6. Records and readiness

For short drafting tasks use a compact working record; for a project-scale audit save a human-readable report (e.g. reports/citation-audit.md) and a structured occurrence ledger (e.g. reports/citation-audit.tsv) with at least:

    occurrence_id | manuscript_path | locator | cite_key | claim | source_id | version | source_urls | accessed_at | identity | metadata | publication_status | support | evidence_locator | evidence_summary | reviewer_mode | action | reason

Include bibliography/source-level results separately where reused across occurrences. Summarize counts of unique keys, occurrences, checked/unchecked, mismatches, unsupported and blocked items; reconcile to the actual inventory, not a sample. Cite-key or claim changes invalidate dependent decisions; store manuscript, bibliography and report hashes with the existing harness snapshot. Mark the citations check passed only after the requested full inventory is reconciled and material identity, metadata, status and support issues are resolved; if any essential check is missing, state the blocker and keep readiness incomplete. For no citations, verify the actual manuscript contains no external claims needing references before using not_applicable. Do not infer a pass from a clean local extraction or successful tool exit.

When using this repository's harness, put the actual citation audit report/ledger in the citations check artifacts and use the existing paper_gate.py freshness mechanism. That program verifies recorded checks and hashes, not citation truth or completeness independently. This protocol is enforced through the selected skill's workflow, not a new automatic hook or a universal parser. No full-text access, payment or private manuscript upload is implied; send only necessary public bibliographic identifiers/search terms to external databases unless authorized otherwise.

## 7. Optional upstream adapters (not dependencies)

Use the local protocol by default. If a user has already installed and reviewed a compatible upstream skill, the host may invoke it explicitly (or read its skill and dependencies), translate its actual evidence/receipts into the local ledger, and reconcile missing axes. Do not install code, request keys, launch an external model or transfer private manuscripts by default. A link or a skill name is not proof of installation or invocation.

| Upstream method | Locally adopted feature | Optional adapter and limit |
| --- | --- | --- |
| [ARIS citation-audit (Codex)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/skills-codex/citation-audit/SKILL.md) | Identity/metadata/context separation, final independent review and evidence receipt | Use for final audit when installed and compatible; inspect actual reviewer independence, access, verdict and dependencies. Same-family review is not independent cross-family validation. |
| [ARIS citation-crosscheck (Codex)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/skills-codex/citation-crosscheck/SKILL.md) | Independent record reconstruction and field comparison | Use for high-risk metadata/author disputes; no attested isolation means heuristic, not blind certification. It does not verify claim support. |
| [Nature Skills nature-ref-verifier](https://github.com/Yuan1z0825/nature-skills/blob/main/skills/nature-ref-verifier/SKILL.md) | Multi-source fallback, field-level checks, early-access/version conflicts | Optionally invoke for metadata; inspect actual source responses and do not use a single failed lookup as fabrication evidence. |
| [Nature Paper Skills claim-source-verification](https://github.com/Boom5426/Nature-Paper-Skills/blob/main/skills/core/claim-source-verification/SKILL.md) | Proposer/skeptic separation, evidence locators, rejected pairings | Optionally invoke per material claim; no source access means no semantic confirmation. |
| [Nature Paper Skills citation-verifier](https://github.com/Boom5426/Nature-Paper-Skills/blob/main/skills/core/citation-verifier/SKILL.md) | Local placeholders, duplicate keys, identifier and field hygiene | Optionally invoke its local checks; not a replacement for external metadata and source support. |
| [K-Dense citation-management](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/citation-management/SKILL.md) | Discovery, identifier resolution, evidence-based bibliography generation | If installed, use its actual metadata/validation tools; a DOI resolution check alone does not match fields or verify semantics. |
| [BeforeSubmitSkill](https://github.com/thinkwee/BeforeSubmitSkill) | Final submission checklist as an optional separate review | No code copied; repository-level review only, detailed implementation/compatibility not validated in this integration. Use existing harness for the default final gate. |

No upstream implementation, script, vendor assets or dependency is vendored. Upstream versions are not pinned/installed; links document method provenance, not reproducible execution of third-party software. Security scans do not establish scientific accuracy. Before enabling an external adapter, inspect its current license, pinned revision, dependencies and permissions; run its tests and verify that the host can actually invoke it.

## 8. Regression scenarios (design cases, not executed model evaluations)

- DOI resolves to a different title: mismatch, never keep just because resolution succeeded.
- No DOI for a real conference paper: resolve official proceedings; absence of DOI alone is not a defect.
- Genuine paper supports retrieval recall but the draft claims answer accuracy: contradicted or partial; narrow or replace.
- A cited table is behind a paywall and only the abstract is available: detailed result unavailable; do not approve it.
- Same reference supports one sentence and contradicts another: verify per occurrence, not per key only.
- Online-first and issue-year disagree: inspect actual version/venue, not a guessed year.
- Retracted source used as ordinary positive evidence: flag and resolve; historical discussion is different.
- Identical semantic verdict from one context repeated twice: never call it independent.
- Changed citation sentence after a prior pass: invalidate that occurrence; final gate must use current hashes.
- Grammar-only edit: preserve existing citation binding; no whole-paper search.
- Network rate limit: record unavailable; no fabricated source, no green verdict.

These are acceptance examples for future runtime tests. This integration does not claim a measured improvement in citation error rates, live external tool tests, or original publisher certification.
