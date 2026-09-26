#!/usr/bin/env python3
"""Check README entries and keep contributor-facing lists in sync.

Stdlib only. Run from the repository root:

    python3 scripts/check_readme.py

Exits 1 if any error is found. Warnings are printed but do not fail.
CONTRIBUTING.md is the source of truth for type labels; the README
`### Section` headings under `## Resources` are the source of truth for
sections. Everything else is checked against those two.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ENTRY = re.compile(
    r"^- \[(?P<title>.+?)\]\((?P<url>\S+?)\) `(?P<type>[a-z]+)` — (?P<desc>.+)$"
)
YEAR = re.compile(r"\b(1[89]\d\d|20\d\d)\b")
LINK = re.compile(r"\[[^\]]*\]\((\S+?)\)")
MAX_DESC = 250
HYPE = re.compile(
    r"\b(canonical|landmark|definitive|de[- ]facto|most[- ]cited|state[- ]of[- ]the[- ]art"
    r"|flagship|load[- ]bearing|industry[- ]standard|gold[- ]standard|seminal"
    r"|best[- ]in[- ]class|world[- ]leading|groundbreaking|cutting[- ]edge|revolutionary"
    r"|the (?:most|clearest|leading|strongest|best|only)"  # unsupported superlatives
    r"|every\b[^.;]*\bshould)\b",  # prescriptive "every team should read"
    re.IGNORECASE,
)
# Rules reported as warnings. A rule graduates to an error by leaving this set.
WARN_RULES = {"year"}


def url_key(url: str) -> str:
    """Normalise a URL so the same work under different links collides."""
    if m := re.search(r"arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})", url):
        return "arxiv:" + m.group(1)
    if m := re.search(r"(?:doi\.org/|/doi/(?:abs/|full/|fullHtml/|pdf/)?)(10\.\d{4,9}/[^?#\s]+)", url):
        return "doi:" + m.group(1).lower().rstrip("/")
    return re.sub(r"^https?://(www\.)?", "", url).rstrip("/").lower()


def anchor(heading: str) -> str:
    """GitHub-style anchor for a heading."""
    slug = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return slug.replace(" ", "-")


def sentence_count(text: str) -> int:
    text = re.sub(r"\b(et al|e\.g|i\.e|vs|approx|cf|ed|eds|no|vol)\.", "", text)
    return len(re.findall(r"[.!?](?:\s+[A-Z]|$)", text.strip())) or 1


def parse_readme(readme: str):
    """Return (entries, sections, map_anchors, legend_types, notes)."""
    entries, sections, notes = [], [], []
    map_anchors, legend = set(), []
    part, section = None, None
    for n, line in enumerate(readme.splitlines(), 1):
        if line.startswith("## "):
            part, section = line[3:].strip(), None
            continue
        if part == "Resources" and line.startswith("### "):
            section = line[4:].strip()
            sections.append(section)
            continue
        if part == "Resource Map" and line.startswith("| ["):
            if m := re.match(r"\| \[[^\]]+\]\(#([^)]+)\)", line):
                map_anchors.add(m.group(1))
        if line.startswith("**Entry types:**"):
            legend = re.findall(r"`([a-z]+)`", line)
        if section and line.startswith("> Cross-references:"):
            notes.append((n, section, line))
        elif section and line.startswith("- ["):
            entries.append((n, section, line))
    return entries, sections, map_anchors, legend, notes


def check(readme: str, contributing: str, others: dict[str, str], issue_form: str):
    """Return a list of (rule, location, message). Pure: no file access."""
    found = []

    def report(rule, where, msg):
        found.append((rule, where, msg))

    m = re.search(r"type labels: ((?:`[a-z]+` ?)+)", contributing)
    allowed = re.findall(r"`([a-z]+)`", m.group(1)) if m else []
    if not allowed:
        report("sync", "CONTRIBUTING.md", "could not find the 'type labels:' list")

    entries, sections, map_anchors, legend, notes = parse_readme(readme)
    seen: dict[str, int] = {}
    urls_by_section = defaultdict(set)
    used_types = set()

    for n, section, line in entries:
        where = f"README.md:{n}"
        e = ENTRY.match(line)
        if not e:
            report("format", where, "entry does not match "
                   "'- [Author(s) — Title (Year)](url) `type` — Contribution.'")
            continue
        title, url, typ, desc = e["title"], e["url"], e["type"], e["desc"]
        used_types.add(typ)
        urls_by_section[section].add(url_key(url))
        if " — " not in title:
            report("format", where, "title must be 'Author(s) — Title (Year)'")
        if not url.startswith("https://"):
            report("https", where, f"use https: {url}")
        if allowed and typ not in allowed:
            report("type", where, f"unknown type `{typ}` (allowed: {', '.join(allowed)})")
        key = url_key(url)
        if key in seen:
            report("duplicate", where, f"same work as README.md:{seen[key]} ({url})")
        else:
            seen[key] = n
        if not YEAR.search(title):
            report("year", where, "title has no year")
        if not desc.endswith("."):
            report("format", where, "contribution sentence must end with a full stop")
        if len(desc) > MAX_DESC:
            report("length", where, f"contribution is {len(desc)} chars (max {MAX_DESC})")
        if h := HYPE.search(desc):
            report("hype", where, f"unsupported ranking or hype term: '{h.group(0)}'")
        if sentence_count(desc) > 1:
            report("sentences", where, "contribution should be one sentence")

    # Cross-reference notes must point at entries that really live elsewhere.
    by_anchor = {anchor(s): s for s in sections}
    for n, section, line in notes:
        for clause in line.split(";"):
            target = re.findall(r"\]\(#([a-z0-9\-]+)\)", clause)
            if not target:
                continue
            home = by_anchor.get(target[-1])
            if home is None:
                report("xref", f"README.md:{n}", f"unknown section anchor #{target[-1]}")
                continue
            for url in LINK.findall(clause):
                if url.startswith("#"):
                    continue
                if url_key(url) not in urls_by_section[home]:
                    report("xref", f"README.md:{n}", f"{url} is not an entry in '{home}'")

    missing = [s for s in sections if anchor(s) not in map_anchors]
    for s in missing:
        report("map", "README.md", f"section '{s}' is missing from the Resource Map")
    for a in sorted(map_anchors - set(by_anchor)):
        report("map", "README.md", f"Resource Map links to #{a}, which is not a Resources section")

    if legend and set(legend) != used_types:
        report("sync", "README.md", f"Entry types legend {sorted(legend)} != types in use {sorted(used_types)}")

    for name, text in others.items():
        labels = re.findall(r"`([a-z]+)`", " ".join(
            line for line in text.splitlines() if re.search(r"(?i)types?[: ]|type labels", line)
            and "`paper`" in line))
        if allowed and labels and sorted(set(labels)) != sorted(allowed):
            report("sync", name, f"type labels {sorted(set(labels))} != CONTRIBUTING.md {sorted(allowed)}")
        if allowed and not labels:
            report("sync", name, "type label list not found")

    form_types = _dropdown(issue_form, "type")
    form_sections = [s for s in _dropdown(issue_form, "section") if s != "Unsure"]
    if allowed and sorted(form_types) != sorted(allowed):
        report("sync", "add-resource.yml", f"type options {form_types} != CONTRIBUTING.md {allowed}")
    if form_sections != sections:
        report("sync", "add-resource.yml", "section options must match README Resources sections, in order "
               f"(missing: {[s for s in sections if s not in form_sections]}, "
               f"extra: {[s for s in form_sections if s not in sections]})")
    return found


def _dropdown(form: str, field_id: str) -> list[str]:
    """Options of a dropdown in a GitHub issue form (no YAML dependency)."""
    m = re.search(rf"id: {field_id}\n(.*?)(?=\n  - type:|\Z)", form, re.S)
    if not m:
        return []
    return re.findall(r"^\s+- (.+)$", m.group(1).split("options:", 1)[-1], re.M)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    read = lambda p: (root / p).read_text(encoding="utf-8")  # noqa: E731
    others = {p: read(p) for p in ("AGENTS.md", "CLAUDE.md", ".github/pull_request_template.md")}
    findings = check(read("README.md"), read("CONTRIBUTING.md"), others,
                     read(".github/ISSUE_TEMPLATE/add-resource.yml"))
    errors = [f for f in findings if f[0] not in WARN_RULES]
    warnings = [f for f in findings if f[0] in WARN_RULES]
    for level, items in (("warning", warnings), ("error", errors)):
        for rule, where, msg in items:
            print(f"{where}: {level} [{rule}] {msg}")
    entries = len(parse_readme(read("README.md"))[0])
    print(f"\n{entries} entries checked: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
