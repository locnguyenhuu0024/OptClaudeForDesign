---
name: visual-validation
description: "Validate an implemented UI against real screenshots, Figma/design references, responsive viewports and visual regressions. Use when asked to compare screenshot to design, visually QA a page, fix spacing mismatch, inspect rendered UI, screenshot review, or detect visual regression. Do not claim visual validation without a render."
user-invocable: true
---

# Evidence-based visual QA

Follow `docs/VISUAL_QA.md`, scoped to the current change.

1. Identify reference(s), target screen, viewport, state, design baseline and expected behavior.
2. Run the actual app/preview only if environment and permissions permit; capture screenshots in ignored scratch output, or use supplied images.
3. Inspect layout, alignment, type, spacing, clipping, responsive behavior, selected/loading/error/empty states and accessibility clues.
4. Compare like-for-like viewport/content/state; separate intentional deviations from defects.
5. Prioritize observed defects with exact region, condition, user impact and minimal fix.
6. Hand off defect list to **one designated writer**. Re-render after fixes and report evidence with paths.
7. If no image or renderer is available, mark **VISUAL QA BLOCKED** and explain reproducible verification steps.

**Output:** actual evidence paths, viewports/states checked, severity-ordered defects, explicit pass/fail/blocked status.
**Boundary:** This skill is for review, not permission to silently edit or claim test results.
