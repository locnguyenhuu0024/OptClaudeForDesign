# Visual verification and UX quality gates

## Gate 0 — Prepare evidence
Record: commit/working-tree status, product route/screen, design reference,
render command/environment, viewport sizes, relevant UI states and source files.
If screenshots are supplied, inspect them rather than inferring their contents.

## Gate 1 — Render the app
Web: use the repository's actual package manager/dev server. Use an already-installed
browser automation tool (Playwright, browser MCP, equivalent) when available.
Do not silently install dependencies. Capture screenshots in a scratch
directory such as `.design-output/<task>/` (gitignored).

Desktop/SwiftUI: build/launch the app if tools and a supported host are available;
capture native screenshots, inspect focus/hover/window resizing; run the app's UI
tests where present. Do not claim iOS simulator verification without a simulator.

If runtime/browser/screenshot access is missing, mark the verification as **BLOCKED**
with the specific missing command or permission, and give reproduction instructions.

## Gate 2 — Compare visual and behavioral outcomes
For each required viewport (e.g. 1440px desktop, 768px tablet, 390px mobile,
or task-specific sizes) inspect:
- Composition, balance, responsive rearrangement, clipping and overflow
- Heading hierarchy, line breaks, typography rhythm, alignment and spacing
- Token consistency, iconography, loading skeleton/empty state coherence
- Form behavior, keyboard focus, escape/close paths, dialogs/popovers,
  hover/pressed/disabled and any errors/success states relevant to that screen
- Accessible names, contrast, visible focus, reduced motion as applicable
- Ref/screenshot mismatch: visual change vs intentional deviation

For each claimed issue: identify file/element/viewport/state, observable
difference, impact, minimal fix and priority. Don't report invented pixels or
contrast ratios.

## Gate 3 — Check code and interactions
Run the narrowest available checks for the affected app:
- linter / typecheck / build
- relevant component + interaction tests
- keyboard navigation and responsive checks
- a11y automation when installed plus manual review for critical flow

## Gate 4 — Iterate, but bound cost
One writer takes severity-ordered feedback. Re-render the *same* states after
changes. Target at most two focused visual-polish iterations. If not converging,
report what is missing (brief, references, renderer, architecture) rather than
escalating effort blindly.

## Gate 5 — Acceptance report

```markdown
## UI verification — <task>
- Build / test: PASS | FAIL | BLOCKED (commands and summary)
- Visual QA: PASS | FAIL | BLOCKED (actual screenshot paths)
- Viewports and states actually checked:
- Critical/major issues remaining:
- Files changed:
- Intentional design deviations:
- Follow-up tasks:
```

**Never equate a passing build with a passing screenshot review.**
A screenshot file's existence is not evidence that someone inspected its content.
