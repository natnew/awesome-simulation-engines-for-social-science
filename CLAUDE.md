# CLAUDE.md

## What this repository is

A curated, public awesome list: **Awesome Learned Social Simulation Engines**. It is a maintained technical index, not an application codebase and not a marketing page. The product is `README.md` under `## Resources` — annotated links organised by domain section.

Help with: README maintenance, PR review, issue triage, contribution review, link-quality checks, section placement, duplicate detection, and concise maintainer comments. There is no build, test, or runtime to operate.

## Scope — what belongs

- Primary research, maintained tools, canonical datasets, and benchmarks that advance the **learned simulation of social systems**.
- Each entry must state a **contribution to a simulation engine**, not just its subject.

## Scope — what does not belong

- Generic AI/ML material with no social-simulation contribution.
- Promotional pages, thin wrappers, unmaintained tools, low-signal blog posts.
- Resources that duplicate an existing entry without adding distinct value.

## Awesome-list quality standards

- Prefer canonical sources: DOIs, publisher pages, official repositories, datasets, docs, or durable project pages over thin wrapper or aggregator pages.
- Each entry must clear the CONTRIBUTING quality bar: best available resource for the concept (not merely convenient); contribution clear to a newcomer; stable link.
- Preserve the existing taxonomy and the contribution-annotation format — they are the asset. Do not restructure without clear justification.
- The domain sections are the **primary** taxonomy. The Functional lens (reconstruct / simulate / plan / calibrate / validate / risk) is a **secondary**, cross-cutting view, currently piloted only on Existing Systems.

## README formatting rules

Canonical entry format (see `CONTRIBUTING.md`):

```
- [Author(s) — Title (Year)](url) `type` — One sentence on what it contributes to the simulation engine.
```

- Type labels: `paper` `book` `article` `tool` `framework` `course` `dataset` (CONTRIBUTING is canonical; the README legend lists only the types currently in use, e.g. `chapter` appears, `course` does not — keep the legend in step with actual entries).
- Use an em dash (`—`) between author(s) and title, and before the one-line contribution.
- One entry per list item; entries sit under an existing `### Section` heading.
- The one-liner states the **contribution**, neutrally and in one sentence. No second sentence of marketing.
- When adding a section to the Resource Map table, link the anchor (`#section-slug`) and add a "what it contributes" cell.

## Link quality rules

- Prefer DOI > publisher / official project page > stable mirror. Avoid blog posts, link shorteners, and aggregators where a canonical source exists.
- Internal links and heading anchors must resolve — the `Links` workflow (`.github/workflows/links.yml`) gates this offline on every PR.
- External links are swept weekly and on demand; `403`/`429` are treated as reachable (publisher bot-blocks), so do not "fix" a link purely on a CI 403.
- For a broken-link fix, record the replacement source in the PR or issue.

## Neutral description style

- Concise, neutral, technically precise. State what the resource contributes.
- Remove or neutralise: promotional language ("best", "revolutionary"), time-sensitive claims ("new", "latest"), rankings, pricing, and unsupported superlatives.
- No vendor hype, no sales framing, no personal or biographical framing.
- Use clear, curated, deliberate, high-signal phrasing.

## Section placement rules

- Every resource falls under an existing `### Section`. Match by **engine function**, not surface topic (e.g. a calibration method goes under Uncertainty Quantification / Evaluation, not under whatever domain it was demonstrated on).
- A new section changes the shape of the list: discuss in an issue first (use the "Propose a new section" form). A section with fewer than three quality entries is usually better as additions to an existing one.
- Respect existing cross-reference notes ("listed under X, deliberately not duplicated") — they prevent duplication.

## Duplicate checking rules

- Before accepting an entry, search the README for the title, author, and URL.
- Check cross-referenced sections, not just the proposed one — the same work may legitimately be referenced from two places via a cross-reference note rather than duplicated.
- If a near-duplicate exists, prefer improving the existing entry over adding a second.

## PR triage workflow

1. Confirm the PR is focused (one section or a small batch of related resources).
2. Check entry format, type label, and that each one-liner states a contribution.
3. Verify links are stable and resolve; confirm no duplicate (including cross-referenced sections).
4. Confirm section placement matches engine function; a new/changed section should reference a prior issue.
5. Decide using the disposition guide below; keep the contributor moving.

## Issue-to-entry workflow

- **Add-a-resource** issues carry the citation, link, type, proposed section, and one-line contribution. Format the final entry and place it under the named section (or correct the placement).
- **Broken-link** issues: confirm the breakage is real (not a transient 403/429), then apply the suggested replacement or find a canonical one.
- **Propose-a-section** issues: assess durability and seed entries before any structural change.
- **Question / scope** issues: answer concisely against the scope rules above.

## Dispositions — when to accept, edit, request changes, close, or park

- **Accept as-is** — meets the format and quality bar, correct section, stable link, no duplicate.
- **Edit as maintainer** — the entry is sound but needs a small safe fix (wording, type label, em dash, anchor, neutralising a promotional phrase). Make the fix directly rather than asking the contributor for a trivial revision.
- **Request changes** — a substantive gap only the contributor can resolve: missing contribution rationale, weak/unstable source, wrong section needing their input.
- **Close** — out of scope, promotional, duplicate with no added value, or weakens the list; explain why, warmly.
- **Park** — plausible but needs discussion (e.g. a new section, a borderline-fit resource); label it and note what would unblock it.

## Maintainer fixes — make small safe changes directly

Small, safe corrections are made by the maintainer rather than bounced back to the contributor: formatting, type labels, em dashes, anchor links, neutralising promotional or time-sensitive wording, obvious link corrections, and minor placement moves. Reserve "request changes" for decisions only the contributor can make.

## Contributor communication style

- Warm, concise, respectful, low-friction. Thank the contributor; lead with what works.
- Be specific about any change needed and why it matters to the list.
- Default to lowering contributor effort — fix the small things yourself.
- Push back respectfully only when a change would weaken quality, clarity, or credibility.

## Repository conventions

- `.github/ISSUE_TEMPLATE/` holds the issue forms (add-resource, broken-link, propose-section, question-scope) and `config.yml` (blank issues disabled, links to CONTRIBUTING). `pull_request_template.md` mirrors the entry format and review checklist.
- `CITATION.cff` makes the list citable; keep author and metadata accurate, and do not invent ORCID, affiliation, DOI, or release fields.
- Several directories are local-only (gitignored) and not part of the public list — do not reference them from public files or assume they ship.
- Do not push directly to `main` for non-trivial changes; prefer a focused branch and review. Keep documentation public-ready and concise.
