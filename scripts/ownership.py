#!/usr/bin/env python3
"""Manage an optional local per-project native Edit/Write ownership manifest.

Usage:
  python3 scripts/ownership.py init
  python3 scripts/ownership.py grant src/App.tsx ui-implementer
  python3 scripts/ownership.py grant src/App.tsx ui-implementer --agent-id <runtime-id>
  python3 scripts/ownership.py release src/App.tsx
  python3 scripts/ownership.py show

The manifest lives in .claude/state/ownership.json (gitignored).
Do not use this as a multi-process lock: writes are not serialized against other agents.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / ".claude" / "state" / "ownership.json"


def relpath(path: str) -> str:
    p = (ROOT / path).resolve()
    try:
        rel = p.relative_to(ROOT.resolve())
    except ValueError:
        raise ValueError("path must be inside the project root") from None
    if rel.as_posix() in {".", ""}:
        raise ValueError("must grant a file, not repository root")
    return rel.as_posix()


def load() -> dict:
    if FILE.exists():
        data = json.loads(FILE.read_text(encoding="utf-8"))
        if not isinstance(data.get("owners"), dict):
            raise ValueError("invalid ownership manifest")
        return data
    return {"version": 1, "owners": {}}


def save(data: dict) -> None:
    FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = FILE.with_suffix(".tmp")
    try:
        tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(tmp, FILE)
    finally:
        if tmp.exists():
            tmp.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="cmd", required=True)
    commands.add_parser("init")
    commands.add_parser("show")
    grant = commands.add_parser("grant")
    grant.add_argument("path")
    grant.add_argument("agent_type")
    grant.add_argument("--agent-id")
    release = commands.add_parser("release")
    release.add_argument("path")
    args = parser.parse_args()
    data = load()
    if args.cmd == "init":
        save(data)
    elif args.cmd == "grant":
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", args.agent_type):
            parser.error("agent_type must be a simple agent identifier or main")
        entry = {"agent_type": args.agent_type}
        if args.agent_id:
            entry["agent_id"] = args.agent_id
        data["owners"][relpath(args.path)] = entry
        save(data)
    elif args.cmd == "release":
        data["owners"].pop(relpath(args.path), None)
        save(data)
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
