# AGENTS.md

Operating protocol for AI coding agents working in this repository.

Claude Code should read `CLAUDE.md` first, then use this file as the shared repository contract. Other agents should start here. Follow repository-local guidance over generic awesome-list assumptions.

## Repository North Star

This is a public, maintained awesome list: **Awesome Learned Social Simulation Engines**. The `README.md` is the product — a durable, high-signal, navigable map of the learned simulation of social systems, for readers, contributors, and research agents.

The list is curated, not accumulated. Each entry must state a **contribution to a simulation engine**, not merely its subject. Selectivity, durability, clear placement, and neutral description quality matter more than volume. There is no build, test, or runtime to operate.

## Agent Role

Agents may help with:

* README maintenance when explicitly asked
* New entry review and formatting
* Pull request review
* Issue triage (add-resource, broken-link, propose-section, question-scope)
* Broken-link checks
* Duplicate detection, including across cross-referenced sections
* Section placement by engine function
* Description tightening and neutralisation
* Maintainer comment drafts
* Small, safe maintainer edits when explicitly requested

Agents must not:

* Add speculative or low-signal entries
* Inflate claims or preserve promotional wording
* Restructure the taxonomy without explicit instruction and a prior issue
* Run broad formatting sweeps
* Edit unrelated or local-only files
* Collapse a single contribution into a structural change
* Touch protected areas unless explicitly instructed

## Read Order

Before reviewing or editing, read in this order:

1. `README.md` — scope, taxonomy, the Resource Map, the Functional lens, formatting, and existing examples
2. `CONTRIBUTING.md` — entry format, quality bar, and PR expectations
3. `.github/ISSUE_TEMPLATE/` — `add-resource`, `broken-link`, `propose-section`, `question-scope`
4. `.github/pull_request_template.md` — entry format and review checklist
5. `CLAUDE.md` — maintainer judgement, dispositions, and Claude-specific review format
6. `docs/` — field-guide notes for context, where a section needs background
7. Recent issues and merged PRs for maintainer precedent

Do not assume the generic awesome-list pattern overrides this repository's structure.

## Repository Facts

* The product is `README.md` under `## Resources` — annotated links grouped by `### Section` headings.
* The **domain sections are the primary taxonomy**. The **Functional lens** (reconstruct / simulate / plan / calibrate / validate / risk) is a secondary, cross-cutting view, currently piloted only on Existing Systems.
* The Resource Map groups sections into navigation tiers; the sections themselves remain the taxonomy.
* Some sections carry explanatory text or a functional-lens table before their entries. Preserve it.
* `CONTRIBUTING.md` asks for one PR per section or per small batch of related resources.
* New entries sit under an existing `### Section`. A new section changes the shape of the list and must be discussed in a `propose-section` issue first; a section with fewer than three quality entries is usually better as additions to an existing one.
* For tool or library submissions, prefer the official repository or project page over a package registry or marketing page.
* Descriptions are concise, neutral, and state the contribution in one sentence.

## Scope Rules

Belongs:

* Primary research, papers, and technical reports advancing the learned simulation of social systems
* Maintained tools, frameworks, and libraries across the simulation stack
* Canonical datasets and benchmarks for social dynamics and agent behaviour
* Calibration, simulation-based inference, uncertainty quantification, and validation methods
* Causal inference, policy, and intervention-modelling resources tied to engine function
* Responsible-AI, ethical-risk, and governance resources relevant to social simulation
* Durable books, chapters, courses, and technical explainers that build or explain an engine

Does not belong:

* Generic AI/ML material with no social-simulation contribution
* Promotional pages, thin wrappers, aggregators, or link farms
* Unmaintained tools or low-signal blog posts where a canonical source exists
* Broken or inaccessible links
* Duplicate or near-duplicate resources adding no distinct value
* Speculative entries
* Unsupported ranking, performance, adoption, or novelty claims
* Time-sensitive claims such as "new", "latest", "best", "leading", or "most advanced"
* Pricing claims

## Quality Bar

An entry qualifies when all are true:

* It advances the learned simulation of social systems and fits an existing section by **engine function**.
* It is the best available resource for the concept, not merely a convenient one.
* The one-liner states the **contribution** clearly to a newcomer, in one neutral sentence.
* The link is canonical, durable, and reachable (DOI, publisher, or official project page).
* The resource adds something distinct from existing entries, including cross-referenced ones.
* The formatting matches the canonical entry format below.
* No duplicate or stronger existing equivalent is already present.

## README Formatting Rules

Canonical entry format (`CONTRIBUTING.md` is canonical):

```
- [Author(s) — Title (Year)](url) `type` — One sentence on what it contributes to the simulation engine.
```

* Type labels: `paper` `book` `article` `tool` `framework` `course` `dataset` `chapter`. Keep the README legend in step with the types actually in use.
* Use an em dash (`—`) between author(s) and title, and before the one-line contribution.
* One entry per list item, under an existing `### Section` heading.
* The one-liner states the contribution, neutrally, in one sentence — no second marketing sentence.
* Use HTTPS links and canonical names.
* Preserve heading structure, the Resource Map, the Functional lens, the engine diagram, badges, and anchors.
* When adding a section to the Resource Map table, link the anchor (`#section-slug`) and add a "what it contributes" cell.
* Do not perform broad formatting changes unless explicitly asked.

## Link Quality Rules

* Prefer **DOI > publisher / official project page > stable mirror**. Avoid blog posts, link shorteners, and aggregators where a canonical source exists.
* Repository links point to the main project, not an arbitrary fork.
* Internal links and heading anchors must resolve — the `Links` workflow (`.github/workflows/links.yml`) gates this offline on every PR.
* External links are swept weekly and on demand. `403`/`429` are treated as reachable (publisher bot-blocks) — do not "fix" a link purely on a CI 403.
* For a broken-link fix, record the replacement source in the PR or issue.
* Avoid avoidable tracking parameters and login-gated resources unless the section already accepts them.

## Description Style

Descriptions should be neutral, factual, specific, concise, and useful to a reader scanning quickly. State what the resource contributes to an engine.

Remove or neutralise: promotional language ("best", "revolutionary", "cutting-edge"), time-sensitive claims ("new", "latest"), rankings, pricing, and unsupported superlatives. No vendor hype, no sales framing, no personal or biographical framing.

## Section Placement Rules

1. Match by **engine function**, not surface topic — a calibration method goes under Uncertainty Quantification / Evaluation, not the domain it was demonstrated on.
2. Identify the narrowest accurate existing section.
3. Where two sections fit, choose the one a reader would look in first, and respect existing cross-reference notes ("listed under X, deliberately not duplicated").
4. Do not move many existing entries unless explicitly asked.
5. A new or changed section requires a prior `propose-section` issue; seed it with three or more quality entries before any structural change.
6. If placement is uncertain, state the trade-off and recommend one option.

## Duplicate Checking Rules

Before adding or approving, search the README for:

* The same URL, or the same work under a different URL
* The same paper title or the same author and product name
* Renamed or mirrored repositories
* An existing entry in a nearby or cross-referenced section
* A stronger canonical source already listed

The same work may legitimately be referenced from two places via a cross-reference note rather than duplicated. If a near-duplicate exists, prefer improving the existing entry over adding a second.

## Decision Matrix

| Decision           | Use when                                                                                                  |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| Accept as-is       | In scope, canonical link, correct section, matching format, neutral one-liner, no duplicate.              |
| Edit as maintainer | Sound entry needing a small safe fix: wording, type label, em dash, anchor, placement, or neutralising a phrase. |
| Request changes    | A substantive gap only the contributor can resolve: missing contribution rationale, weak source, wrong section needing their input. |
| Close              | Out of scope, promotional, duplicate with no added value, or weakens the list. Explain why, warmly.       |
| Park               | Plausible but needs discussion: a new section, or a borderline-fit resource. Label it and note what would unblock it. |

Make small, safe corrections directly rather than bouncing them back: formatting, type labels, em dashes, anchors, neutralising wording, obvious link corrections, and minor placement moves. Reserve "request changes" for decisions only the contributor can make.

## Issue-to-Entry Workflow

For `add-resource` issues:

1. Check scope and source quality.
2. Check link quality and reachability.
3. Check for duplicates, including cross-referenced sections.
4. Identify the best section by engine function.
5. Format the entry only if it qualifies; place it under the named section or correct the placement.
6. Recommend accept, maintainer edit, request changes, close, or park, with a concise comment.

For `broken-link` issues:

1. Confirm the breakage is real, not a transient `403`/`429`.
2. Search for a canonical replacement; prefer official sources over mirrors.
3. Preserve the entry if a durable replacement exists; recommend removal only when none does.
4. Record the replacement source and state the action clearly.

For `propose-section` issues: assess durability and seed entries before any structural change.
For `question-scope` issues: answer concisely against the scope rules above.

## Pull Request Review Workflow

1. Read the PR title, description, and diff; confirm it is focused (one section or a small related batch).
2. Confirm it changes only relevant files.
3. Check entry format, type label, and that each one-liner states a contribution.
4. Check each link is canonical, stable, and resolves.
5. Check scope, source quality, and duplicates (including cross-referenced sections).
6. Confirm section placement matches engine function; a new/changed section references a prior issue.
7. Neutralise description language where needed.
8. Decide: accept, maintainer edit, request changes, close, or park.
9. Draft a concise maintainer comment.

Minimise contributor friction. If the resource is clearly suitable and the issue is minor, make the maintainer edit rather than asking the contributor to revise.

## Stop and Ask

Stop and ask the maintainer before:

* Creating or renaming a top-level section
* Reordering large parts of the README
* Changing the Resource Map or Functional lens structure
* Editing the engine diagram, badges, or visual assets
* Changing contribution rules or `CITATION.cff` metadata
* Removing multiple entries
* Making judgement-heavy scope changes
* Editing files unrelated to the stated task

## Protected Areas

Do not create, edit, stage, commit, or push these unless explicitly instructed:

* Badges, the engine diagram, and other visual assets
* The Resource Map and Functional lens scaffolding
* `CITATION.cff` author, ORCID, affiliation, DOI, or release fields (do not invent them)
* Licence text and repository metadata unrelated to the task
* Local-only, gitignored directories such as `specs/`, `private/`, `scratch/`, and `.local/`
* Credentials, secrets, tokens, keys, personal notes, and draft files

If unsure whether a file belongs in the public repository, leave it untouched and explain the concern.

## Git Safety

* Run `git status` before any commit; review staged files and confirm no protected or local-only files are included.
* Do not push directly to `main` for non-trivial changes; prefer a focused branch and review.
* Never push broad unrelated changes with a focused documentation or review task.

## Maintainer Comment Style

Comments should be warm, concise, respectful, and decision-oriented. Thank the contributor, lead with what works, be specific about any change and why it matters to the list, and default to lowering contributor effort.

Prefer:

* "Thank you for the suggestion — this is relevant, the link is canonical, and I would place it under X with a shorter contribution line."
* "Useful resource — I would accept this with a small maintainer edit to remove the ranking claim."
* "Thank you for raising this — I would close it as a duplicate, since the resource already appears under X."
* "I would park this until we have a clearer section for this category."

Avoid long explanations, harsh or defensive wording, and asking contributors for trivial edits the maintainer can safely make.

## Final Response Pattern

When finishing a task, summarise:

* What was reviewed
* The decision or recommended decision
* What changed, if anything
* Any risks or uncertainties
* A suggested maintainer comment, if relevant
* Follow-up needed, if any

Do not modify `README.md` or other files unless explicitly asked.
