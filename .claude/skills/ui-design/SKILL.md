---
name: ui-design
description: "Orchestrate multi-step UX/UI feature design, frontend or SwiftUI implementation and rendered visual verification end-to-end. Use when asked to build or redesign a complete screen, feature or multi-screen flow, coordinate subagents, or implement and validate a new interface. For standalone visual polish or responsive fixes, use a narrower skill."
argument-hint: "[screen, feature, or redesign brief]"
---

# UI design workflow

Request: $ARGUMENTS

1. **Inspect:** identify the product, user task, code framework, tokens, component library, UI screens, existing flows, tests and existing visual references. For screenshots/Figma references, identify what must be preserved.
2. **Route:** consult `docs/SKILL_ROUTING.md` and read task-relevant sections of `docs/ORCHESTRATION.md`. Apply only 1–2 specialist skills (e.g. `ui-art-direction` for visual hierarchy, `ux-flow` for multi-step navigation, `design-system` for shared tokens, `swiftui-native-design` for Apple native UI). XS: no agent; S: one writer; M: 1–3 specialists; L/XL: partition feature/screen modules. Do not load every skill or spawn agents to repeat known context.
3. **Contract:** for M+ summarize goal, non-goals, design direction, affected files, UI states, breakpoints, functional invariants, acceptance criteria and ownership table. Use `docs/TEMPLATES.md`. Obtain design-direction approval before broad redesigns when feasible.
4. **Parallel critique:** delegate independent *read-only* UX architecture (`ux-architect`), visual direction (`visual-director`) and accessibility (`accessibility-auditor`) only when each adds distinct value. Consolidate into one nonconflicting design contract.
5. **Execute:** assign exactly one active writer per file (`ui-implementer` or `ui-polisher`). Use bounded file paths; do not let reviewers edit. Use `design-variant` in isolated worktrees for parallel alternatives on the same file; only the integrator applies the chosen diff.
6. **Verify:** use `docs/VISUAL_QA.md`. Render real UI, inspect screenshot at the agreed viewports/states, execute interaction/build/a11y checks, and ask `visual-qa` to compare if useful. Work to a maximum of two focused polish cycles before escalating or reporting the blockers.
7. **Deliver:** affected paths, design decisions, screenshots/evidence paths, executed commands/results, unresolved issues. Do not fabricate images or verification.

Relevant references: `docs/DESIGN_STANDARDS.md`, `docs/ORCHESTRATION.md`, `docs/VISUAL_QA.md`, `docs/TEMPLATES.md`.

**Shared-file invariant:** parallel research is encouraged; concurrent direct writing to the same path is forbidden. A worktree allows competing versions, not automatic merging.
