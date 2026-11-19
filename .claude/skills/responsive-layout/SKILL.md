---
name: responsive-layout
description: "Adapt a web or app UI to mobile, tablet, desktop, narrow windows, orientation, Dynamic Type and content overflow. Use for responsive design, breakpoint bugs, mobile layout, tablet adaptation, small screens, window resizing, safe areas, or elements clipping/overflowing. Not for unrelated visual redesign."
user-invocable: true
---

# Responsive layout

Read the current layout constraints and actual content before changing breakpoints.

1. Identify target viewports/platform and container behavior; use existing responsive conventions.
2. Define layout transformations for nav, columns, forms, tables, dense data and primary actions across widths.
3. Prefer intrinsic sizing, wrapping and content-driven breakpoints; avoid fixed heights that clip dynamic content.
4. Preserve reading/focus order, touch target accessibility, safe areas, zoom and localization/long labels.
5. Inspect realistic long text, empty and error states, native window resize or web viewport widths.
6. Verify **rendered** screenshots at requested widths and check scroll/overflow. If no renderer, report blocked.

**Output:** breakpoint behavior map, affected components, responsive acceptance tests and observed evidence.
**Boundary:** No new layout library or component rewrite solely to handle a small overflow issue.
