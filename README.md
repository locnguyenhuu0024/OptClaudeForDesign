# OptClaudeForDesign

**A token-conscious, multi-agent UX/UI design operating system for Claude Code.**

OptClaudeForDesign is a **rules and skills template**, not a frontend app. Install its files into the root of a real React, Vue, Svelte, SwiftUI, or other UI repository, then open that repository in Claude Code.

## Why this exists

- Keep visual quality, usability, accessibility, and design-system consistency high.
- Route UX architecture to **Opus 5.5 Medium**, visual exploration and implementation to **Sonnet 5.5 High**, and mechanical polish/visual QA to **Sonnet 5.5 Medium**.
- Use **parallel readers, a single writer per shared file, and parallel reviewers**.
- Explore competing edits to **the same file** only in **isolated Git worktrees**; integrate with an explicit diff review.
- Require a **real rendered screenshot** to justify visual acceptance. A successful build is not visual verification.
- Load guidance progressively rather than sending every guideline to every agent.

These are starting presets, not guarantees about benchmark ranking, quotas, or your account's available models. Pin/adjust them locally after measuring quality and retry cost.

## Automatic UX/UI skill activation

**No slash command required for normal UX/UI requests.** Claude Code matches
the prompt against skill descriptions; only the matching skill body is loaded.
The `CLAUDE.md` router emphasizes choosing the *narrowest* suitable skill,
while custom subagents preload their own role-relevant domain skills.

| Request or task | Auto-matched specialist skill |
|---|---|
| UX journey, onboarding, wireframe, navigation | `ux-flow` |
| Visual concept, typography, polished dashboard | `ui-art-direction` |
| Reusable components and design tokens | `design-system` |
| Mobile/tablet layout, clipping, resize | `responsive-layout` |
| Loading, validation, dialogs and feedback | `interaction-states` |
| WCAG, keyboard, screen reader, focus | `accessibility-review` |
| Screenshot vs reference, visual regression | `visual-validation` |
| SwiftUI macOS/iOS native interface | `swiftui-native-design` |
| Whole feature from design through code and screenshots | `ui-design` |
| Comprehensive read-only experience audit | `ui-review` |

Examples of **natural prompts** (no `/` prefix):

```text
Thiết kế lại UX flow onboarding 3 bước, tối giản thao tác.
Làm giao diện dashboard đẹp hơn, giữ nguyên business logic.
Sửa responsive cho màn hình 390px và lỗi tràn nội dung.
Audit keyboard navigation và màu sắc theo WCAG.
So sánh screenshot hiện tại với bản thiết kế.
Thiết kế cửa sổ Settings bằng SwiftUI native trên macOS.
```

Automatic matching is **model-guided, not guaranteed**. These project skills
only become available when the files are in the Claude Code project's
`.claude/skills/` tree. To debug discovery, ask Claude "What skills are
available?", check skill descriptions or run `/skill-name` directly.
This system never auto-installs dependencies or changes source merely because
a skill has been discovered. See [skill routing and trigger tests](docs/SKILL_ROUTING.md).

## Structure

```text
CLAUDE.md                     # always-loaded, compact project contract
.claude/
  agents/                     # model- and effort-specific specialists
  skills/ui-design/SKILL.md   # end-to-end /ui-design workflow
  skills/ui-review/SKILL.md   # full /ui-review audit
  skills/*/SKILL.md           # 8 narrow, auto-discovered UX/UI skills
  hooks/guard_writes.py       # optional file-ownership guard
  settings.guard.example.json # opt-in hook settings; NOT installed by default
docs/
  DESIGN_STANDARDS.md         # visual, UX and accessibility requirements
  ORCHESTRATION.md            # routing, parallelism and same-file policies
  VISUAL_QA.md                # evidence-based screenshot workflow
  TEMPLATES.md                # task/design/QA contract examples
  SKILL_ROUTING.md            # intent -> skill mapping and trigger tests
scripts/
  ownership.py                # opt-in owner manifest management
tests/
  test_guard_writes.py        # stdlib-only hook unit tests
  test_skill_routing.py       # static skill metadata/preload checks
```

## Install in a product repository

1. Clone or download this rules repository.
2. Copy `CLAUDE.md`, `.claude/agents/`, `.claude/skills/`, `docs/` and (optionally) `scripts/` and `.claude/hooks/` to the **root of the UI project**. Merge any existing `CLAUDE.md` / settings rather than blindly overwriting.
3. From the UI project root, start `claude`. Ask naturally, such as "Improve this dashboard UI and check mobile responsive". Claude should auto-match the relevant skill. Check `/agents` or invoke `/ui-design <brief>` explicitly if necessary.
4. Supply an existing screenshot/design reference if there is one. The agent will inspect the actual framework, components and tokens before changing code.
5. Review the design contract for large changes; require screenshot evidence and verification before accepting the result.

### Suggested prompts

```text
/ui-design Redesign the billing dashboard. Retain the existing component library,
avoid API changes, and verify desktop 1440px + mobile 390px screenshots.

/ui-design Create two competing concepts for the settings screen.
Use isolated worktrees; do not merge without my approval.

/ui-review Audit the account creation flow for accessibility,
interaction states and visual consistency. Do not edit source files.
```

### Optional file-ownership guard

`CLAUDE.md` requires a single writer per file as a workflow rule. For a limited **additional technical guard** against direct `Edit`/`Write` calls:

1. Copy the `PreToolUse` entry from `.claude/settings.guard.example.json` into your existing `.claude/settings.json` (do not replace other settings).
2. Run `python3 scripts/ownership.py grant src/screens/Dashboard.tsx ui-implementer` before assigning this file.
3. For a handoff, `release` and `grant` the new owner.
4. Run `python3 -m unittest discover -s tests -v` to check the guard and static skill contracts.

**Important:** this is not a cross-process lock. It validates declared agent types for the native Edit/Write tools only; Bash, PowerShell, other file-editing tools, external apps and multiple instances of the *same* agent type are not covered. For strict isolation use distinct worktrees and controlled integration. Never claim that a natural-language rule or this optional hook guarantees atomic file locking.

## Claude Code vs Cowork / normal Chat

**Claude Code is the primary runtime** for repository-aware implementation, custom per-agent effort, Git worktrees, builds, screenshot loops and native hooks. **Claude Cowork** can also run agentic workflows and plugins; it is useful for research, creative brief formation and asset review, but this repository's project-local `.claude/agents` and hooks should not be assumed to load in a normal Cowork session. To reuse centrally in Cowork, package the guidance as a Claude Plugin and enable it for your account. **Normal Chat** can use skills but does not execute plugin hooks/sub-agents.

See [Claude Code custom subagents](https://code.claude.com/docs/en/sub-agents), [skills](https://code.claude.com/docs/en/skills), [hooks](https://code.claude.com/docs/en/hooks), [worktrees](https://code.claude.com/docs/en/worktrees) and [Cowork plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

## Scope and trust

- Never overwrite user work, reformat unrelated files, or add dependencies without approval.
- Never claim screenshots, tests, tool results, or successful deployments you did not actually observe.
- Preserve accessibility and behavior when doing visual polish.
- A copy of this repository provides *instructions*, not automatic access to Figma, simulators, browser tools, git credentials, or model entitlements.

License: no license has been assigned yet. Add one before redistributing as an open-source package.
