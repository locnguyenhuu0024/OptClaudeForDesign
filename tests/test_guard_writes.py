"""Unit tests for the optional native Edit/Write guard. stdlib only."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


GUARD_PATH = Path(__file__).resolve().parents[1] / ".claude" / "hooks" / "guard_writes.py"
spec = importlib.util.spec_from_file_location("guard_writes", GUARD_PATH)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "src").mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def manifest(self, owners):
        path = self.root / ".claude" / "state" / "ownership.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"version": 1, "owners": owners}))

    def call(self, tool="Edit", path=None, actor="ui-implementer", agent_id="a-123"):
        return guard.authorize({
            "tool_name": tool,
            "tool_input": {"file_path": str(path or self.root / "src" / "App.tsx")},
            "agent_type": actor,
            "agent_id": agent_id,
        }, self.root)

    def test_disabled_is_noop(self):
        self.assertTrue(self.call()[0])

    def test_authorized_owner(self):
        self.manifest({"src/App.tsx": {"agent_type": "ui-implementer"}})
        self.assertTrue(self.call()[0])

    def test_other_agent_denied(self):
        self.manifest({"src/App.tsx": "ui-implementer"})
        self.assertFalse(self.call(actor="ui-polisher")[0])

    def test_missing_owner_denied(self):
        self.manifest({})
        self.assertFalse(self.call()[0])

    def test_agent_id_pin_denied(self):
        self.manifest({"src/App.tsx": {"agent_type": "ui-implementer", "agent_id": "a-999"}})
        self.assertFalse(self.call()[0])

    def test_agent_id_pin_accepted(self):
        self.manifest({"src/App.tsx": {"agent_type": "ui-implementer", "agent_id": "a-123"}})
        self.assertTrue(self.call()[0])

    def test_outside_root_denied(self):
        self.manifest({})
        self.assertFalse(self.call(path=self.root.parent / "outside.tsx")[0])

    def test_other_tools_not_intercepted(self):
        self.manifest({})
        self.assertTrue(self.call(tool="Read")[0])

    def test_invalid_manifest_denied(self):
        self.manifest({})
        path = self.root / ".claude" / "state" / "ownership.json"
        path.write_text("{bad json")
        self.assertFalse(self.call()[0])

    def test_main_thread_owner(self):
        self.manifest({"src/App.tsx": "main"})
        self.assertTrue(self.call(actor=None)[0])


if __name__ == "__main__":
    unittest.main()
