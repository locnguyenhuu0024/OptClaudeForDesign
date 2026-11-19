# Multi-agent orchestration and quota discipline

Read this document only when planning concurrent UI work or routing nontrivial tasks.

## Skills are domain instructions; subagents are workers

The auto-matching UX/UI skills in `docs/SKILL_ROUTING.md` are lightweight
domain workflows, **not** eight additional always-on agents. Claude Code
discovers a skill from its description, whereas a subagent runs in a separate
context with a model, effort and tool permissions. Preloading a skill in a
subagent injects its full body at spawn time. Limit preloads to the role's
essential skills and only spawn a worker where independent work justifies it.
Skills may be explicitly invoked with `/name` if discovery misses.

## Decision hierarchy
1. Follow the current product's design system and user brief.
2. Prefer completing the task with the fewest agents before maximizing parallelism.
3. Parallelize *independent decision questions* and *independent file sets*; not agents merely looking at the same screen.
4. Bound every subagent with scope, evidence, files, expected output, and stop conditions.
5. A reviewer's critique is advisory. Only the orchestrator owns the final design contract.

## Task tiers (starting presets)

| Tier | Typical work | Main / delegates | Active workers | Approval |
|---|---|---|---:|---|
| XS | Label/spacing/token tweak | Main Sonnet Medium | 0 | Existing direction |
| S | One existing component | Sonnet High implementer | 1 | Scoped contract |
| M | One screen / responsive layout | Main Opus Medium + optional UX Opus Medium, visual Sonnet High, implementer Sonnet High | 1–3 | Design contract |
| L | Cross-screen feature or redesign | Main Opus Medium/High + specialized read-only critiques + disjoint implementers | 2–4 | Direction before broad edit |
| XL | Multi-flow product redesign | Split into L-sized batches, explicit integration and UX audit | 3–5 max per batch | Human checkpoints |

Prefer *main coordinator = Opus 5.5 Medium*, *UX architecture = Opus Medium*,
*visual direction / UI implementation = Sonnet 5.5 High*,
*polish / screenshot QA = Sonnet Medium*. Escalate the effort/model only for demonstrated failure
caused by reasoning complexity. Model availability may vary by account/provider; check /status and /agents.
These presets are hypotheses: track passes, retries, tokens and latency on your own repository.

### Escalation ladder
- Visual tweak unclear? Ask for screenshot or inspect the actual render before raising effort.
- Small code/layout bug? Sonnet Medium -> Sonnet High.
- UX trade-off or cross-screen state conflict? Opus Medium -> Opus High if unresolved.
- Do not automatically retry the same vague task with Max effort; narrow the task and supply evidence first.
- Stop after two nonconvergent screenshot/polish loops; diagnose missing requirements, broken renderer or model mismatch.

## Role-to-agent contract

| Agent | Tools/permission | Output |
|---|---|---|
| `ux-architect` | Read-only | Flows, decisions, state inventory, acceptance |
| `visual-director` | Read-only | Layout, type, spacing and visual direction |
| `accessibility-auditor` | Read-only | Severity-ranked usability/a11y risks |
| `ui-implementer` | Writable owned paths | Minimal code diff + tests |
| `ui-polisher` | Writable owned paths, sequential | Narrow screenshot fixes |
| `visual-qa` | Read source; may run preview/test commands | Screenshot evidence and defects |
| `design-variant` | Isolated worktree | Competing change set, never direct merge |
| `design-integrator` | Main checkout single writer | Reviewed integration and tests |

Read-only agents are limited to `Read, Glob, Grep`; visual-qa has `Bash` to run tests/capture
evidence, which is *not technically read-only*. It is prohibited from modifying product source by policy.

## File ownership: three supported modes

**A. Single writer (default).** Parallel agents inspect the same file and submit critique;
one assigned implementer owns all direct edits. Best for a single JSX/SwiftUI file.

**B. Sequential handoff.** Implementer completes layout, returns diff, releases ownership;
polisher reads latest version and fixes visual defects. Never overlap write windows.

**C. Parallel design variants.** Each `design-variant` runs in `isolation: worktree`
and may edit its own copy of the same path. Compare renders and diffs, choose one,
then `design-integrator` alone applies the reviewed variant to the product checkout.
Do not cherry-pick/merge blindly: semantic and line conflicts remain possible.

Before spawning worktrees, verify actual base ref. Claude Code defaults worktree start
to the default branch, not necessarily the caller's feature HEAD. An optional project
setting `{"worktree":{"baseRef":"head"}}` changes that behavior to the current HEAD
but does not include uncommitted files. Either commit/snapshot necessary source
first or tell the variant agent which changes are missing. Never stash/discard user edits unilaterally.

## Compact task dispatch format

```yaml
task_id: UI-04
purpose: Implement responsive account settings panel
agent: ui-implementer
file_owner: ui-implementer
owned_files:
  - src/features/account/SettingsPanel.tsx
read_only_context:
  - src/styles/tokens.css
  - src/components/FormField.tsx
do:
  - Reuse existing FormField
  - Preserve save/load logic
  - Add keyboard-accessible error summary
do_not:
  - Change backend contracts
  - Add packages
acceptance:
  - Desktop and mobile render without overflow
  - Error states announced and actionable
verification:
  - typecheck
  - screenshot desktop/mobile
stop_if:
  - Existing behavior contradicts contract
```

## Dispatch and integration checks

- Search file ownership **before** launching writers. Same agent *type* may have
multiple concurrent instances; a natural-language owner label does NOT lock file access.
- If ownership scopes overlap, serialize tasks or use separate worktrees.
- Limit context to active task + relevant code + required design contract excerpts.
- Collect concise reports; avoid asking each agent to reread the entire repository.
- Main integrator reviews diffs, runs compilation/typecheck/tests and screenshot checks
after combined changes. File-level compilation does not prove an integrated flow works.
- No unreviewed shell write to shared files, no force push, no silent git checkout/reset.
- Make parallelism conditional: coordination overhead can exceed the saved time/tokens.

## Worktree checks before integration

1. Identify candidate commit SHA and parent/base.
2. Verify intended diff, unexpected paths, dependency changes and behavior.
3. Compare screenshots of same UI states/viewports.
4. Apply selected changes through one writer; resolve conflicts deliberately.
5. Run integrated tests, render screenshots again, record evidence.
