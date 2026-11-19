#!/usr/bin/env python3
"""Optional, deliberately limited Claude Code PreToolUse file-owner check.

When .claude/state/ownership.json is absent, this hook is inactive (allow).
When present, direct Edit/Write calls are denied unless the caller matches the
single declared owner for that relative file. A declaration may also pin agent_id.

IMPORTANT: Bash/PowerShell and other tools can write files without passing this
hook. This is NOT a file lock, concurrency mutex, or security boundary.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def authorize(payload: dict[str, Any], root: Path) -> tuple[bool, str]:
    """Return (allowed, explanation); pure except loading the manifest."""
    if payload.get("tool_name") not in {"Write", "Edit"}:
        return True, "outside Edit/Write scope"
    manifest = root / ".claude" / "state" / "ownership.json"
    if not manifest.exists():
        return True, "owner guard not enabled (no manifest)"
    try:
        config = json.loads(manifest.read_text(encoding="utf-8"))
        owners = config["owners"]
        if not isinstance(owners, dict):
            raise ValueError("owners must be an object")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return False, f"invalid ownership manifest: {exc}"
    file_path = payload.get("tool_input", {}).get("file_path")
    if not isinstance(file_path, str) or not file_path:
        return False, "missing absolute file_path"
    try:
        target = Path(file_path)
        if not target.is_absolute():
            return False, "file_path must be absolute"
        relative = target.resolve().relative_to(root.resolve()).as_posix()
    except (ValueError, OSError):
        return False, "target is outside project root"
    rule = owners.get(relative)
    if isinstance(rule, str):
        rule = {"agent_type": rule}
    if not isinstance(rule, dict):
        return False, f"no owner granted for {relative}"
    actor = payload.get("agent_type") or "main"
    if rule.get("agent_type") != actor:
        return False, f"{relative} owned by {rule.get('agent_type')!r}, caller is {actor!r}"
    if rule.get("agent_id") is not None and rule.get("agent_id") != payload.get("agent_id"):
        return False, f"{relative} is restricted to a different agent_id"
    return True, f"owner verified for {relative}"


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    try:
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict):
            raise ValueError("hook input must be a JSON object")
        allowed, reason = authorize(payload, root)
    except (ValueError, TypeError) as exc:
        allowed, reason = False, f"malformed hook input: {exc}"
    if not allowed:
        print(f"OptClaude file-owner guard: {reason}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
