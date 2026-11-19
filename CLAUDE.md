# OptClaudeForDesign — execution contract

You are working in an actual UI product repository that has adopted OptClaudeForDesign.
Product code and existing design-system conventions outrank generic aesthetics. Preserve functionality.

## Activation and routing
- For UI/UX creation, redesign or UI implementation, apply `/ui-design` (see `.claude/skills/ui-design/SKILL.md`).
- For read-only design/UX/a11y audits, apply `/ui-review`.
- Read only task-relevant sections of `docs/DESIGN_STANDARDS.md`, `docs/ORCHESTRATION.md` and `docs/VISUAL_QA.md`. Do not preload every document.
- Inspect existing code, installed component libraries, typography, tokens, breakpoints, assets, design references and tests before proposing new ones.
- Size task XS/S/M/L/XL; use the fewest agents and lowest sufficient effort.

## Design gates
1. Establish user goal, platform, target viewport, existing state and acceptance criteria.
2. For M+ agree on a compact design contract; never invent product requirements.
3. Implement scoped changes with a **single active writer per file**.
4. Render the UI and inspect screenshots + relevant interaction states; run appropriate checks.
5. Report evidence, remaining defects, files changed and tests; never claim unobserved verification.

## Multi-agent safety
- Parallelize read-only UX, visual, and accessibility investigations where worthwhile.
- Split writable work by independent files. Never delegate concurrent writes to the same checkout/file.
- Multiple agents may propose changes to the same file read-only; one assigned writer integrates.
- Alternative same-file implementations require separate Git worktrees and explicit human-reviewed integration. Worktree isolation does not eliminate merge conflicts.
- Verify worktree baseline (current HEAD vs default branch), and account for uncommitted changes.
- If an agent reports conflicting requirements, stop that branch, resolve with the user or record the trade-off; do not silently overwrite.
- Reviewers do not edit product source. Do not bypass safety hooks or ownership gates.

## Nonnegotiable quality
- Follow the product's established design system, accessibility baseline, semantic structure and platform conventions.
- Cover default, loading, empty, error, success, hover, focus, disabled and selected states where applicable.
- Avoid incidental refactoring, new dependencies, fabricated assets and speculative redesign.
- No success claim without actual build/test evidence; no visual acceptance without inspected render/screenshots.
- If rendering is unavailable, report *visual QA blocked* and provide a reproducible verification plan.

## Model guidance
Default main orchestrator: **Opus 5.5 Medium**; UX decisions: Opus Medium;
visual implementation: **Sonnet 5.5 High**; polish/visual QA: Sonnet Medium.
Escalate on demonstrated uncertainty, not on task size alone. Agent frontmatter pins
models; check `/status`, `/agents` and account availability before relying on these presets.
