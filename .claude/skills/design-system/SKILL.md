---
name: design-system
description: "Design or evolve a reusable UI component system, theme tokens, typography scales, spacing scales, component variants and cross-screen consistency. Use when asked about design system, UI kit, component library, reusable buttons/forms, design tokens, theme consistency or component architecture. Not for single pixel tweaks."
user-invocable: true
---

# Design system and components

Treat the project's current components and tokens as ground truth until a redesign is explicitly approved.

1. Inventory existing token names, theme modes, typography, spacing, radii, colors and component APIs; find near-duplicates first.
2. Define or refine **semantic tokens** (surface, text, border, intent, focus), not disconnected per-screen literals.
3. Model components with explicit variants/sizes/states, accessible semantics and predictable composition.
4. Preserve public props and existing behavior unless migration scope is approved; avoid broad global CSS overrides.
5. For shared changes, provide affected screens, migration plan, compatibility and visual regression coverage.
6. Document usage examples, forbidden combinations and testable acceptance criteria.

**Output:** token/component decision table, migration/impact map, compatibility risks, review checklist.
**Boundary:** Shared components/tokens get one writer at a time; parallel agents may inspect or propose but not simultaneously edit them.
