# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This repository is a public, maintained awesome list — **Awesome Learned Social Simulation Engines** — not an application codebase. There is no build, lint, or test workflow to run for normal review tasks. The `README.md` is the product.

Claude Code should read this file first, then use `AGENTS.md` as the shared, tool-agnostic operating protocol. This file is an orientation layer; `AGENTS.md` holds the full protocol. Do not duplicate long sections from it here.

## North Star

* Preserve `README.md` as the canonical public artefact — a curated, functional map of systems that learn, perturb, and validate social dynamics.
* Keep the list selective, durable, technically useful, neutral, and easy to scan.
* Each entry must state a **contribution to a simulation engine**, not just its subject.
* Help the maintainer make fast, consistent, low-friction decisions.
* Prefer small, precise edits over broad rewrites.
* Do not broaden the list beyond the learned simulation of social systems and clearly adjacent technical areas already represented in the README.

## Claude's Role

Claude may assist with:

* PR review and issue triage (add-resource, broken-link, propose-section, question-scope)
* README entry review and formatting
* Broken-link investigation
* Duplicate detection, including across cross-referenced sections
* Section placement by engine function
* Neutral description rewrites
* Maintainer comment drafts
* Small safe maintainer edits when explicitly asked
* Improvements to agent instruction files (`CLAUDE.md`, `AGENTS.md`) when asked

Claude must not:

* Add entries without checking scope, link quality, duplicates, and placement
* Invent facts about a resource, or invent `CITATION.cff` metadata (ORCID, affiliation, DOI, release)
* Preserve promotional, ranking, pricing, novelty, adoption, or performance claims without strong evidence
* Restructure the taxonomy, Resource Map, or Functional lens without explicit instruction and a prior issue
* Edit unrelated files or touch protected areas unless instructed
* Ask contributors to make trivial fixes the maintainer can safely make

## Repository Facts

* `AGENTS.md` contains the full tool-agnostic operating protocol.
* `CONTRIBUTING.md` contains contributor-facing rules and the entry format.
* `.github/ISSUE_TEMPLATE/` contains the public issue forms and `config.yml`; `.github/pull_request_template.md` mirrors the entry format and review checklist.
* `README.md` contains the introduction, the engine diagram, the **Resource Map**, the **Functional lens**, and the main list under `## Resources`.
* The **domain sections are the primary taxonomy**. The Functional lens (reconstruct / simulate / plan / calibrate / validate / risk) is a secondary, cross-cutting view, piloted only on Existing Systems.
* The list uses bullet entries plus a few tables (Resource Map, the Existing Systems lens). Match the surrounding section exactly.
* New entries sit under an existing `### Section`. New sections are handled separately via a `propose-section` issue.
* `docs/` holds field-guide notes for background; several directories (`specs/`, `private/`, `scratch/`, `.local/`) are local-only and gitignored — do not reference them from public files.

## Always-Loaded Context

Keep this file short. Use this routing:

* Need the full agent protocol → read `AGENTS.md`
* Need contribution rules and the quality bar → read `CONTRIBUTING.md`
* Need PR process → read `.github/pull_request_template.md`
* Need contributor expectations → inspect `.github/ISSUE_TEMPLATE/`
* Need style examples or placement → inspect the target section in `README.md`
* Need background on a section → inspect `docs/`
* Need maintainer precedent → inspect recent issues and merged PRs where available

## First-Pass Workflow

For any PR, issue, or README task:

1. Read the user request.
2. Read the relevant issue, PR, diff, or target README section.
3. Check repository scope (learned simulation of social systems).
4. Check `CONTRIBUTING.md` if the task concerns a submission.
5. Check neighbouring entries for style, format, and placement.
6. Search for duplicates, including cross-referenced sections.
7. Verify the link where tools allow.
8. Inspect the resource enough to understand what it contributes.
9. Choose the smallest useful action.
10. Produce a concise decision, edit, or maintainer comment.

## Entry Checklist

Before recommending acceptance or adding an entry, confirm:

* In scope, and contributes to an engine (not just its subject)
* The best available resource for the concept, not merely convenient
* Credible, canonical, durable link (DOI, publisher, or official project page)
* No duplicate, including cross-referenced sections
* Correct section, matched by engine function
* Canonical entry format matched (see below)
* Neutral one-sentence contribution, no hype, no unsupported claims
* No avoidable tracking parameters
* No unnecessary new section

## Canonical Entry Format

```
- [Author(s) — Title (Year)](url) `type` — One sentence on what it contributes to the simulation engine.
```

* Type labels: `paper` `book` `article` `tool` `framework` `course` `dataset` `chapter`. `CONTRIBUTING.md` is canonical; keep the README legend in step with the types actually in use.
* Use an em dash (`—`) between author(s) and title, and before the one-line contribution.
* One entry per list item, under an existing `### Section` heading.
* The one-liner states the contribution, neutrally, in one sentence — no second marketing sentence.
* When adding a section to the Resource Map table, link the anchor (`#section-slug`) and add a "what it contributes" cell.

## Source Preference

Prefer: DOIs, publisher pages, official repositories and documentation, papers, technical reports, benchmarks, datasets, durable project pages, and maintained tools and libraries. For a tool, prefer the official repository or project page over a package registry or marketing page.

Treat cautiously: launch and vendor posts, thin wrappers, newsletter and social posts, unmaintained repositories, aggregators and link farms, pages dominated by sales language, and time-sensitive comparisons.

## Description Rules

Descriptions should be concise, neutral, technically precise, and state what the resource contributes to an engine. One sentence, no second sentence of marketing.

Remove or neutralise: "best", "latest", "new", "most advanced", "powerful", "revolutionary", "cutting-edge", "game-changing", "industry-leading", "fastest", rankings, pricing, and unsupported performance, adoption, or maturity claims. No vendor hype, no sales framing, no personal or biographical framing. Use clear, curated, deliberate, high-signal phrasing.

## Section Placement

Match by **engine function**, not surface topic — a calibration method goes under Uncertainty Quantification / Evaluation, not the domain it was demonstrated on.

| Situation                              | Action                                                       |
| -------------------------------------- | ------------------------------------------------------------ |
| Exact fit in an existing section       | Place there.                                                 |
| Fits two sections                      | Choose the section a reader would look in first; respect cross-reference notes. |
| Similar to neighbouring entries        | Place near them if local ordering allows.                    |
| New theme with one entry               | Park, or place in the nearest broader section.               |
| New theme with several strong entries  | Suggest a new section via a `propose-section` issue; do not create it unless asked. |
| Unclear placement                      | Explain the options briefly and recommend one.               |

Respect existing cross-reference notes ("listed under X, deliberately not duplicated") — they prevent duplication.

## PR Triage

| Decision        | Use when                                                                                  |
| --------------- | ----------------------------------------------------------------------------------------- |
| Accept as-is    | Scope, link, placement, format, and contribution line are all sound.                      |
| Maintainer edit | Strong resource needing only minor wording, type label, em dash, anchor, link, or placement fixes. |
| Request changes | A substantive gap only the contributor can resolve: missing contribution rationale, weak source, wrong section needing their input. |
| Close           | Out of scope, duplicate, promotional, broken with no replacement, or weakens the list.    |
| Park            | Promising but immature, needs a taxonomy decision, or needs maintainer judgement.         |

## Issue Triage

Suggestion (`add-resource`) issues:

* Strong, in scope, canonical → draft the entry and recommend acceptance.
* Strong but wording or placement needs work → recommend a maintainer edit.
* Missing evidence → ask for minimal clarification.
* Duplicate → close with a pointer to the existing entry.
* Out of scope → close politely.
* Premature or taxonomy-dependent → park.

`broken-link` issues:

* Confirm the breakage is real — `403`/`429` are treated as reachable (publisher bot-blocks), so do not "fix" a link purely on a CI 403.
* Find a canonical replacement first; prefer official sources over mirrors.
* Remove only when no durable replacement exists; record the replacement source.

Internal links and heading anchors must resolve — the `Links` workflow (`.github/workflows/links.yml`) gates this offline on every PR.

## Small Safe Fix Rule

When a resource is suitable and the issue is minor, make or recommend a maintainer edit rather than asking the contributor to revise. Small safe fixes include: tightening a description, removing hype, fixing punctuation or an em dash, correcting a type label, fixing an anchor, correcting placement, replacing a non-canonical URL, and removing tracking parameters. Reserve "request changes" for decisions only the contributor can make.

## Stop and Ask

Stop before:

* Creating or renaming a top-level section
* Reordering large parts of the README
* Changing the Resource Map or Functional lens structure
* Editing the engine diagram, badges, or visual assets
* Changing contribution rules or `CITATION.cff` metadata
* Removing several entries
* Making broad scope decisions
* Editing files unrelated to the stated task

## Protected Areas

Do not edit unless explicitly instructed:

* Badges and the engine diagram
* The Resource Map and Functional lens scaffolding
* `CITATION.cff` author, ORCID, affiliation, DOI, or release fields
* Licence text and repository metadata unrelated to the task
* Local-only, gitignored directories (`specs/`, `private/`, `scratch/`, `.local/`)
* Credentials, secrets, personal notes, and draft files

## Contributor Communication

Warm, concise, respectful, low-friction. Thank the contributor and lead with what works; be specific about any change and why it matters to the list; default to lowering contributor effort. Push back respectfully only when a change would weaken quality, clarity, or credibility.

Templates:

* **Accept** — "Thank you — this looks relevant, the link is canonical, and the placement works. I would accept this."
* **Maintainer edit** — "Thank you — useful resource. I would accept it with a small maintainer edit to tighten the contribution line and keep the wording neutral."
* **Request changes** — "Thank you for the suggestion. I think this could fit, but I would ask for a little more context on why this is the canonical source and where it belongs."
* **Duplicate** — "Thank you — I would close this as a duplicate, since the resource already appears under [section]."
* **Out of scope** — "Thank you for sharing this. I would close it because it sits outside the current scope of the list."
* **Park** — "Thank you — this may be worth revisiting, but I would park it until the list has a clearer section for this category."

## Output Format

For PR or issue review, respond with:

* **Decision**: accept, maintainer edit, request changes, close, or park
* **Reason**: 1–3 bullets
* **Suggested README entry**, if useful
* **Suggested maintainer comment**
* **Files changed**, if any
* **Remaining uncertainty**, if any

## Git and Editing Rules

* Do not modify `README.md`, `CONTRIBUTING.md`, `.github` templates, or other files unless explicitly asked.
* Run `git status` before any commit; confirm no protected or local-only files are staged.
* Do not push directly to `main` for non-trivial changes; prefer a focused branch and review. Keep documentation public-ready and concise.
