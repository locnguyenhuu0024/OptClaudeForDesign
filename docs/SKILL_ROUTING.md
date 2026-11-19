# Automatic UX/UI skill routing

This is a **policy and discovery aid**, not a deterministic event engine.
Claude Code loads descriptions of model-invocable project skills and chooses relevant ones.
The full SKILL.md content is loaded **on use**, except skills explicitly preloaded
by a subagent's `skills:` field (full body is loaded when that subagent starts).
Manual `/skill-name` commands remain available.

## Decision tree

1. If request is a **multi-stage design + implementation + visual validation feature**, use `ui-design` as coordinator. Apply only domain skills that materially change implementation.
2. If request is a **complete read-only audit** spanning multiple UX/UI dimensions, use `ui-review` as coordinator. Use one or two focused specialist skills.
3. Otherwise select **the single narrowest skill** below; optionally a second for a distinct quality dimension.
4. Use `swiftui-native-design` only for actual Apple native UI work, alongside one other specialty if needed.
5. Keep default loading small: avoid indiscriminately loading every skill, spawning a subagent for every skill, or re-invoking identical skill bodies.

| User intent / natural-language signals | Skill | Outcome |
|---|---|---|
| user journey, onboarding flow, IA, wireframe, navigation map | `ux-flow` | navigable flow, states, acceptance |
| visually polish, beautiful UI, landing aesthetics, typography, visual hierarchy | `ui-art-direction` | visual direction and composition |
| design tokens, theme, reusable components, variant system | `design-system` | consistency and migration impact |
| responsive, mobile, tablet, clipping, overflow, resize | `responsive-layout` | adaptive layout checks |
| states, dialogs, loading, errors, validation, animation behavior | `interaction-states` | state machine and tests |
| WCAG, contrast, keyboard, screen reader, VoiceOver, a11y | `accessibility-review` | evidence-ranked accessibility issues |
| screenshot comparison, actual render, visual regression, design mismatch | `visual-validation` | screenshot-based findings |
| SwiftUI, native macOS/iOS/iPadOS | `swiftui-native-design` | platform-specific behavior |
| whole feature, multiple screens, implement+verify | `ui-design` | design-to-implementation orchestration |
| full audit without editing | `ui-review` | prioritized UX/UI audit |

## Compositions

- **New dashboard**: `ui-design` + `ui-art-direction`, add `design-system` only if shared tokens/components must change.
- **Fix mobile overflow**: `responsive-layout` alone; `visual-validation` if screenshots are available.
- **Improve checkout UX**: `ux-flow` + `interaction-states`; `ui-design` only if implementation requested.
- **Audit an existing screen**: `ui-review`; `accessibility-review` if a11y is explicitly in scope.
- **Mac SwiftUI redesign**: `ui-design` + `swiftui-native-design` + one visual/UX specialty only when needed.
- **Match a Figma screenshot**: `ui-art-direction` for direction + `visual-validation` after actual rendering.

## Tests for routing behavior

In a UI repository with the files installed, ask these prompts **without** slashes
and observe which skills Claude announces/loads:

| Prompt | Expected primary skill |
|---|---|
| "Map the onboarding journey and simplify navigation." | `ux-flow` |
| "Make this dashboard visually more polished; keep its behavior." | `ui-art-direction` |
| "Create reusable button variants and semantic design tokens." | `design-system` |
| "Fix the mobile overflow and narrow-window layout." | `responsive-layout` |
| "Define loading, error and success states for checkout." | `interaction-states` |
| "Audit keyboard, labels and WCAG contrast." | `accessibility-review` |
| "Compare the actual page screenshot with the reference." | `visual-validation` |
| "Redesign this macOS SwiftUI preferences window." | `swiftui-native-design` + coordinator if implementation |
| "Build and verify a new settings flow end to end." | `ui-design` |

**Negative tests:** "fix API error", "update dependency", "format a SQL query",
and "edit README" should not invoke UI design skills.

**Limits:** Description matching is model-guided, not guaranteed. If a skill
doesn't trigger, check its description and verify discovery, then invoke `/name`
explicitly. A user can override visibility with `skillOverrides` or turn off
a skill. Do not force auto-writes or install hooks solely to trigger skills.

## Automated CI vs manual runtime testing

`tests/test_skill_routing.py` checks metadata, uniqueness, route coverage,
and the existence of subagent preload targets. It **does not prove** the Claude
model will choose the right skill from natural-language prompts. Run the above
positive/negative prompts in a Claude Code session for end-to-end validation.
