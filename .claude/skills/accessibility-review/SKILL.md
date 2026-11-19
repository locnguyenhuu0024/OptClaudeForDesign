---
name: accessibility-review
description: "Review UI for WCAG 2.2 AA accessibility, keyboard navigation, focus order, screen-reader semantics, color contrast, labels, touch targets and reduced motion. Use for accessibility, a11y, WCAG, contrast, keyboard-only, VoiceOver, screen reader or usability for disabled users. Not a generic styling audit."
user-invocable: true
---

# Accessibility review

Use the project's stated target; otherwise use WCAG 2.2 AA as the **web target**, adapting appropriately to native platforms.

1. Inspect semantic hierarchy, headings/landmarks, names/labels, reading order, form error associations and announcements.
2. Check logical tab/keyboard/focus behavior including open/close/escape and focus restoration.
3. Measure actual contrast when colors are available; do not assert a pass from a screenshot alone.
4. Inspect target sizes, reflow, reduced motion, zoom/Dynamic Type and color-independent status.
5. Use runtime keyboard/screen reader tests or existing test tools when permitted; distinguish **verified** from **code-inferred** issues.
6. Rank findings Critical/Major/Minor and include specific remediation and regression tests.

**Output:** evidence-ranked issues with affected screen/element and measurable fixes.
**Boundary:** Read-only unless a bounded remediation task is explicitly assigned to a writer; automated testing is not certification.
