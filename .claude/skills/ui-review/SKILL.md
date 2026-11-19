---
name: ui-review
description: "Run a comprehensive read-only UX/UI audit spanning usability, visual hierarchy, design consistency, responsive behavior and accessibility across a screen or flow. Use when asked to critique, assess or audit the whole experience without editing. For a focused screenshot comparison or WCAG audit, use visual-validation or accessibility-review instead."
argument-hint: "[screen, flow, or screenshots]"
---

# Read-only UI/UX audit

Target: $ARGUMENTS

1. Read the relevant design contract and existing system, not arbitrary external aesthetics.
2. If an actual render is available, inspect screenshots and working interaction states. If not, label findings as code-inferred or unverified.
3. Audit user goal completion, navigation, hierarchy, typography, spacing rhythm, contrast, responsive layout, copy, empty/error/loading/disabled/focus states, and accessibility.
4. Consult `docs/SKILL_ROUTING.md` and invoke only a focused specialty when it adds distinct evidence (e.g. `ux-flow`, `visual-validation` or `accessibility-review`). Use specialized `visual-qa` and `accessibility-auditor` agents only for bounded checks on complex flows.
5. Return a concise table: severity (critical/major/minor), location, observed evidence, user impact, recommended fix, acceptance test. Distinguish subjective visual taste from objective usability violations.
6. Do not write product source; offer an implementation plan separately.

Consult `docs/DESIGN_STANDARDS.md` and `docs/VISUAL_QA.md` as needed.
