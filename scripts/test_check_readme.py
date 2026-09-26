"""Each rule in check_readme.py must fire on a seeded fault and stay quiet on a clean list.

Run from the repository root: python3 -m unittest discover -s scripts
"""
import unittest

from check_readme import check, url_key

CONTRIBUTING = "Use one of these type labels: `paper` `tool`\n"
OTHERS = {"AGENTS.md": "* Types: `paper`, `tool`.\n"}
FORM = """  - type: dropdown
    id: type
    attributes:
      options:
        - paper
        - tool
  - type: dropdown
    id: section
    attributes:
      options:
        - Alpha
        - Beta
        - Unsure
"""
README = """## Resource Map

| [Alpha](#alpha) | x |
| [Beta](#beta) | x |

**Entry types:** `paper` · `tool`

## Resources

### Alpha

- [Doe — A Paper (2020)](https://arxiv.org/abs/2001.00001) `paper` — Shows one thing.

> Cross-references: [Roe 2021](https://example.org/tool) is under [`### Beta`](#beta).

### Beta

- [Roe — A Tool (2021)](https://example.org/tool) `tool` — Provides another thing.
"""


def rules(readme=README, contributing=CONTRIBUTING, others=OTHERS, form=FORM):
    return {rule for rule, _, _ in check(readme, contributing, others, form)}


class CheckReadme(unittest.TestCase):
    def test_clean_fixture_passes(self):
        self.assertEqual(rules(), set())

    def test_seeded_faults(self):
        entry = "- [Roe — A Tool (2021)](https://example.org/tool) `tool` — Provides another thing."
        cases = {
            "format": entry.replace(" `tool` — ", " `tool` - "),
            "https": entry.replace("https://example.org/tool", "http://example.org/tool2"),
            "type": entry.replace("`tool`", "`course`"),
            "year": entry.replace(" (2021)", ""),
            "length": entry.replace("another thing.", "x" * 300 + "."),
            "hype": entry.replace("another", "the canonical"),
            "sentences": entry.replace("thing.", "thing. Freely available online."),
        }
        for rule, bad in cases.items():
            with self.subTest(rule=rule):
                self.assertIn(rule, rules(README.replace(entry, bad)))

    def test_duplicate_detects_same_arxiv_id_across_url_forms(self):
        dup = "- [Doe — Again (2020)](https://arxiv.org/pdf/2001.00001) `paper` — Repeats it.\n"
        self.assertIn("duplicate", rules(README + dup))

    def test_cross_reference_must_point_at_real_entry(self):
        self.assertIn("xref", rules(README.replace("(https://example.org/tool) is under", "(https://example.org/gone) is under")))

    def test_resource_map_must_list_every_section(self):
        self.assertIn("map", rules(README.replace("| [Beta](#beta) | x |\n", "")))

    def test_label_and_section_lists_stay_in_sync(self):
        self.assertIn("sync", rules(others={"AGENTS.md": "* Types: `paper`.\n"}))
        self.assertIn("sync", rules(form=FORM.replace("        - Beta\n", "")))
        self.assertIn("sync", rules(readme=README.replace("`paper` · `tool`", "`paper`")))

    def test_url_key_normalises_doi_and_arxiv(self):
        self.assertEqual(url_key("https://doi.org/10.1000/ABC"), url_key("https://dl.acm.org/doi/10.1000/abc"))
        self.assertEqual(url_key("https://arxiv.org/abs/2001.00001"), url_key("https://arxiv.org/html/2001.00001"))


if __name__ == "__main__":
    unittest.main()
