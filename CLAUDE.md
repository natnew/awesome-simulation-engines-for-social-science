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
- Domain sections are the primary taxonomy. The Resource Map and Functional lens (only piloted in the Existing Systems table) are protected scaffolding.
- Type labels: the README legend (`README.md`, "Entry types") matches what is in use, including `chapter`. `CONTRIBUTING.md` and the PR template omit `chapter` and list the unused `course`. Treat that as known drift: don't copy it, and fix it only when asked.
- Never invent resource facts or `CITATION.cff` metadata. Strip hype, rankings, and unsupported "state of the art" or "most-cited" claims from new or edited lines; don't sweep existing entries unless asked.

## Repo gotchas

- `.gitignore` lists `docs/`, but the three `docs/*.md` files are tracked. Edits to them commit normally. A new file there needs `git add -f`, and only when asked.
- `CHANGELOG.md`, `specs/`, and `.claude/` are gitignored, so never reference them from public files.
- `skills/changelog` and `skills/feature-spec` are generic templates, not part of this repo's workflow. `feature-spec` expects a `specs/roadmap.md` that doesn't exist. Don't invoke either unless asked.
- `.codex/` and `.trae/` hold empty placeholders for other tools. Ignore them.
- `.github/workflows/claude.yml` runs Claude on `@claude` mentions in issues and PRs. In that context, answer in the thread using the output format below.

## Workflow

1. Read the request, then the issue, PR diff, or target section.
2. Check scope and contribution against `AGENTS.md` → Curation Standard.
3. Search for duplicates across the whole README by URL, alternate URL (arXiv vs DOI), title words, and author or product name: `grep -n -i '<fragment>' README.md`. Check cross-reference notes too.
4. Verify external links with WebFetch where available. `403`/`429` count as reachable; don't "fix" a link on that alone.
5. Choose the smallest useful action. Make small safe fixes (wording, em dash, type label, anchor, tracking parameters, placement) yourself instead of asking the contributor.

For a batch of several independent PRs, issues, or a broken-link sweep, parallel subagents are fine for link checks and duplicate searches. For a single entry, work inline.

## Verification before commit

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
