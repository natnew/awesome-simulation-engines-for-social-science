# AGENTS.md

Shared operating protocol for **Awesome Learned Social Simulation Engines**. Claude Code reads `CLAUDE.md` first; other agents start here. Repository-local guidance takes precedence over generic awesome-list conventions.

## Purpose and Authority

`README.md` is the product: a selective, durable map of learned social simulation. Each entry must explain its **contribution to a simulation engine**, not just its subject. Prioritise quality, neutral descriptions, and navigation over volume. There is no application build, test suite, or runtime to operate.

Assist with entry and PR review, issue triage, link and duplicate checks, placement, wording, and maintainer comment drafts. **Modify files only when explicitly asked**, and keep edits focused. Within an authorised editing task, make small safe corrections directly; reserve contributor revision requests for substantive gaps.

## Read Order

Before reviewing or editing, read:

1. `README.md` — scope, taxonomy, Resource Map, Functional lens, and entry examples.
2. `CONTRIBUTING.md` — canonical entry format, quality bar, and PR expectations.
3. `.github/ISSUE_TEMPLATE/` — resource, broken-link, section, and scope forms.
4. `.github/pull_request_template.md` — submission checklist.
5. `CLAUDE.md` — maintainer judgement and Claude-specific review format.
6. Relevant `docs/` notes when section background is needed.
7. Recent issues and merged PRs for maintainer precedent.

## Curation Standard

Accept only resources that advance learned social simulation: primary research and technical reports; maintained tools and frameworks; canonical datasets and benchmarks; calibration, simulation-based inference, uncertainty, and validation methods; causal and policy modelling; responsible-AI, ethical-risk, and governance work; and durable books, chapters, courses, or explainers tied to engine function.

Reject generic AI/ML material without that contribution, speculative or low-signal entries, promotional pages, thin wrappers, aggregators, link farms, unmaintained tools, inaccessible resources, and duplicates without distinct value. Prefer the best available source for a concept over a convenient one.

Every addition or approval must pass these checks:

* **Contribution:** specific, factual, clear to a newcomer, and expressed in one neutral sentence. Remove hype, rankings, pricing, time-sensitive claims, unsupported performance/adoption/novelty claims, and personal or biographical framing.
* **Source:** canonical, durable, reachable, and compliant with the link rules below.
* **Distinct value:** search the whole README, including nearby and cross-referenced sections, for matching URLs, alternate URLs for the same work, titles, author/product names, renamed or mirrored repositories, and stronger existing equivalents. Prefer improving a near-duplicate or using a cross-reference over duplicating an entry.
* **Placement and format:** follow the rules below; do not turn one contribution into a structural change.

## Entry Format and Placement

Use the canonical format from `CONTRIBUTING.md`:

```text
- [Author(s) — Title (Year)](url) `type` — One sentence on what it contributes to the simulation engine.
```

* Use canonical names, HTTPS, and both em dashes. One list item and one contribution sentence per entry.
* Types: `paper`, `book`, `article`, `tool`, `framework`, `course`, `dataset`, `chapter`. Keep the README legend aligned with types in use.
* `scripts/check_readme.py` enforces this section mechanically (format, labels, duplicate works, https, cross-reference targets, Resource Map coverage, and that label and section lists in `CONTRIBUTING.md`, this file, `CLAUDE.md`, the PR template, and the `add-resource` form match the README). CI blocks on its errors; its warnings mark wording rules still being phased in. Judgement checks — contribution, source quality, placement — remain yours.
* Entries belong under an existing `### Section` within `## Resources`. Domain sections are the primary taxonomy; the Resource Map groups them for navigation. The Functional lens (reconstruct / simulate / plan / calibrate / validate / risk) is secondary and piloted only on Existing Systems.
* Choose the narrowest accurate section by **engine function**, not surface topic: calibration belongs under Uncertainty Quantification / Evaluation rather than its demonstration domain. If two sections fit, choose where readers would look first and respect cross-reference notes. Explain uncertain placement and recommend one option.
* Preserve headings, anchors, explanatory text, tables, and protected structures. No broad formatting sweeps or bulk moves unless explicitly requested.
* New or changed sections require explicit instruction and a prior `propose-section` issue; establish durability and at least three quality seed entries before restructuring. For an authorised Resource Map addition, include the section anchor and a “what it contributes” cell.

## Link Rules

* Prefer **DOI > publisher / official project page > stable mirror**. For tools, use the official repository or project page over registries or marketing pages; repository links must target the main project, not arbitrary forks.
* Avoid link shorteners, unnecessary tracking parameters, and login-gated sources unless the section accepts them.
* Internal links and anchors must resolve. `.github/workflows/links.yml` checks these offline on PRs; external links are swept weekly and on demand, and broken ones are reported in a single open `Link report` issue labelled `broken-link`. Triage that issue with the broken-link rules below.
* `403`/`429` responses are treated as reachable publisher bot-blocks, not evidence of breakage by themselves.
* For broken links, confirm the failure, seek a canonical replacement, and preserve the entry when a durable replacement exists. Recommend removal only if none exists; record replacement sources in the issue or PR.

## Review and Triage

For PRs, read the title, description, and diff; require relevant files only and one section or a small related batch. Apply the curation, format, placement, and link checks above, including the prior issue for taxonomy changes. Choose a disposition and draft a concise maintainer comment.

| Decision | Use when |
| --- | --- |
| Accept as-is | All checks pass. |
| Edit as maintainer | A sound entry needs minor wording, type, punctuation, anchor, link, or placement fixes. |
| Request changes | A substantive gap requires contributor input, such as missing rationale or source evidence. |
| Close | Out of scope, promotional, duplicate without added value, or otherwise weakens the list; explain respectfully. |
| Park | Plausible but needs taxonomy discussion or maintainer judgement; label it and state what would unblock it. |

Apply the same checks to `add-resource` issues; draft an entry only if it qualifies. Use the link rules for `broken-link`, assess durability and seed entries for `propose-section`, and answer `question-scope` against the curation standard. Recommend small maintainer fixes instead of asking contributors for trivial revisions; apply them only within authorised editing scope.

## Approval Boundaries and Protected Areas

Unless already explicitly authorised, stop and ask before creating or renaming top-level sections, substantially reordering the README, changing contribution rules, removing multiple entries, making judgement-heavy scope changes, or editing unrelated files.

Do not create, edit, stage, commit, or push any of these without explicit instruction:

* Badges, the engine diagram, or other visual assets.
* Resource Map or Functional lens scaffolding.
* `CITATION.cff` metadata, including author, ORCID, affiliation, DOI, and release fields; never invent values.
* Licence text or repository metadata unrelated to the task.
* Local-only or gitignored directories such as `specs/`, `private/`, `scratch/`, and `.local/`.
* Credentials, secrets, tokens, keys, personal notes, or drafts.

If a file's suitability for the public repository is uncertain, leave it untouched and explain why.

## Git and Reporting

* Before committing, run `python3 scripts/check_readme.py` and `git status`, and inspect staged files; exclude unauthorised protected, local-only, and unrelated changes.
* Use a focused branch and review for non-trivial changes; do not push them directly to `main` or bundle unrelated changes.
* Report what was reviewed, the decision, changes, relevant checks, remaining risks or uncertainties, and any follow-up. Include a suggested maintainer comment when relevant.
* Comments should be warm, concise, respectful, and decision-oriented: thank the contributor, lead with what works, and explain any correction and its value. Avoid long or defensive explanations and unnecessary contributor work.
