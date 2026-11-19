"""Static checks for auto-discoverable project skills and specialist preloads.

Does NOT prove model-dependent automatic invocation. See docs/SKILL_ROUTING.md.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".claude" / "skills"
AGENTS_DIR = ROOT / ".claude" / "agents"
SPECIALIST = {
    "ux-flow": ("journey", "flow"),
    "ui-art-direction": ("visual", "typography"),
    "design-system": ("tokens", "components"),
    "responsive-layout": ("responsive", "mobile"),
    "interaction-states": ("loading", "states"),
    "accessibility-review": ("wcag", "keyboard"),
    "visual-validation": ("screenshot", "render"),
    "swiftui-native-design": ("swiftui", "macos"),
}
PRELOADS = {
    "ux-architect": ("ux-flow", "interaction-states"),
    "visual-director": ("ui-art-direction",),
    "ui-implementer": ("design-system",),
    "ui-polisher": ("ui-art-direction",),
    "visual-qa": ("visual-validation",),
    "accessibility-auditor": ("accessibility-review",),
    "design-variant": ("ui-art-direction",),
    "design-integrator": ("design-system",),
}

def frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if match is None:
        raise AssertionError(f"missing YAML frontmatter: {path}")
    return match.group(1)

def scalar(metadata: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", metadata)
    if not match:
        raise AssertionError(f"missing {key}")
    return match.group(1).strip().strip('"').strip("'")

class SkillRoutingContractTests(unittest.TestCase):
    def test_all_expected_skills_exist(self):
        available = {p.parent.name for p in SKILLS_DIR.glob("*/SKILL.md")}
        self.assertTrue(set(SPECIALIST).issubset(available))
        self.assertTrue({"ui-design", "ui-review"}.issubset(available))
        self.assertEqual(len(available), 10)

    def test_auto_invocation_metadata(self):
        for path in SKILLS_DIR.glob("*/SKILL.md"):
            with self.subTest(skill=path.parent.name):
                meta = frontmatter(path)
                description = scalar(meta, "description")
                self.assertGreater(len(description), 60)
                self.assertLess(len(description), 520)
                self.assertNotIn("disable-model-invocation: true", meta)
                self.assertNotIn("user-invocable: false", meta)
                self.assertGreater(len(path.read_text(encoding="utf-8").splitlines()), 12)

    def test_domain_specific_descriptions(self):
        for skill, terms in SPECIALIST.items():
            with self.subTest(skill=skill):
                description = scalar(frontmatter(SKILLS_DIR / skill / "SKILL.md"), "description").lower()
                for term in terms:
                    self.assertIn(term, description)

    def test_preloaded_skill_targets(self):
        for agent, skills in PRELOADS.items():
            with self.subTest(agent=agent):
                meta = frontmatter(AGENTS_DIR / f"{agent}.md")
                field = re.search(r"(?ms)^skills:\n((?:  - [a-z0-9-]+\n?)+)", meta)
                self.assertIsNotNone(field, "agent needs specialist skills preloaded")
                listed = tuple(re.findall(r"(?m)^  - ([a-z0-9-]+)$", field.group(1)))
                self.assertEqual(listed, skills)
                for skill in listed:
                    self.assertTrue((SKILLS_DIR / skill / "SKILL.md").is_file())

    def test_router_docs_reference_all(self):
        doc = (ROOT / "docs" / "SKILL_ROUTING.md").read_text(encoding="utf-8")
        for skill in SPECIALIST:
            self.assertIn(f"`{skill}`", doc)

if __name__ == "__main__":
    unittest.main()
