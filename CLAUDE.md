# CLAUDE.md

Claude-specific operating layer for **Awesome Learned Social Simulation Engines**, a curated awesome list, not an application. `README.md` is the product. There is no build, package, or test suite; the only automated check is the `Links` workflow.

`AGENTS.md` is the full, tool-agnostic protocol (curation standard, link rules, triage dispositions, protected areas). Read it before any review or edit; this file adds only routing, repo gotchas, and Claude's output format. Do not copy its content here.

## Route to the authoritative file

| Need | Read |
| --- | --- |
| Curation standard, link rules, triage table, approval boundaries | `AGENTS.md` |
| Contributor-facing entry format and quality bar | `CONTRIBUTING.md` |
| PR checklist / issue forms (`add-resource`, `broken-link`, `propose-section`, `question-scope`) | `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/` |
| Style, placement, and cross-reference notes for a section | The target `### Section` in `README.md` |
| Section background | `docs/00-landscape-map.md`, `docs/01-core-concepts.md`, `docs/02-existing-systems.md` |
| Maintainer precedent | Recent merged PRs and closed issues on GitHub |

`README.md` is ~100 KB. Read the outline (`grep -n '^#' README.md`) and then only the sections you need.

## Invariants

- Entry format, one list item per resource, under an existing `### Section` in `## Resources`:
  ```text
  - [Author(s) — Title (Year)](url) `type` — One neutral sentence on what it contributes to the simulation engine.
  ```
- Place by **engine function**, not surface topic. Respect `> Cross-references: … deliberately not duplicated` notes; they are deliberate de-duplication, so never re-add a resource they point elsewhere.
- Sections are the primary taxonomy; `AGENTS.md` → Entry Format and Placement lists the boundaries between overlapping sections. The Resource Map (tiers, body order, and a Function column) and the Existing Systems function table are protected scaffolding, and the checker fails if the map and body disagree.
- Type labels: `paper` `book` `article` `tool` `framework` `course` `dataset` `chapter`. `CONTRIBUTING.md` is the source list; `scripts/check_readme.py` fails if this file, `AGENTS.md`, the PR template, or the `add-resource` form drift from it, or if the README "Entry types" legend differs from the labels in use.
- Never invent resource facts or `CITATION.cff` metadata. Contributions are one neutral sentence of at most 250 characters, without rankings, superlatives, adoption claims, or institution name-drops; the checker rejects common hype terms, but unsupported claims in plain words are still yours to remove.

## Repo gotchas

- `CHANGELOG.md`, `specs/`, and `.claude/` are gitignored local working files, so never reference them from public files.
- `.github/workflows/claude.yml` runs Claude on `@claude` mentions in issues and PRs. In that context, answer in the thread using the output format below.

## Workflow

1. Read the request, then the issue, PR diff, or target section.
2. Check scope and contribution against `AGENTS.md` → Curation Standard.
3. Search for duplicates across the whole README by title words and author or product name: `grep -n -i '<fragment>' README.md`. Check cross-reference notes too. The checker catches identical works by URL, arXiv ID, or DOI, but not a preprint linked by title elsewhere.
4. Verify external links with WebFetch where available. `403`/`429` count as reachable; don't "fix" a link on that alone.
5. Choose the smallest useful action. Make small safe fixes (wording, em dash, type label, anchor, tracking parameters, placement) yourself instead of asking the contributor.

For a batch of several independent PRs, issues, or a broken-link sweep, parallel subagents are fine for link checks and duplicate searches. For a single entry, work inline.

## Verification before commit

- Run `python3 scripts/check_readme.py` (stdlib only). It must report 0 errors: entry format, type labels, duplicate works (arXiv/DOI-aware), https, cross-reference targets, Resource Map coverage, list sync, contribution length (≤250 chars), single sentence, and hype or superlative terms. The only warning left is a missing year in the title; don't add new ones. CI runs it with its tests (`python3 -m unittest discover -s scripts`).
- Heading anchors and relative links must resolve. CI runs `lychee --offline --include-fragments "**/*.md"`, so run it locally if `lychee` is installed. Otherwise, check any new `#anchor` against its `###` heading by hand. Renaming a heading breaks Resource Map and cross-reference anchors.
- Re-read the diff: the only changes should be what was asked, the format should match neighbouring entries exactly, and no protected area should be touched.
- Run `git status` and confirm that no local-only or unrelated files are staged.

## Stop and ask

Stop before you create or rename a section, change the Resource Map, Functional lens, engine diagram, or badges, remove several entries, change contribution rules or `CITATION.cff`, reorder large parts of the README, or edit files outside the task. New sections go through a `propose-section` issue first.

## Output format (PR / issue review)

- **Decision**: accept · maintainer edit · request changes · close · park (criteria in `AGENTS.md`)
- **Reason**: 1–3 bullets
- **Suggested README entry**, if any
- **Suggested maintainer comment**: warm, concise, and led by what works. For example: "Thank you — useful resource. I'd accept it with a small maintainer edit to keep the contribution line neutral."
- **Files changed**, if any
- **Remaining uncertainty**, if any

Modify files only when explicitly asked. Use a focused branch for non-trivial changes, never a direct push to `main`.
