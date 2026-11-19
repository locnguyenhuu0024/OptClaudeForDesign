# UX/UI quality standard

Use existing project tokens and components as the source of truth. These guidelines
apply where the product does not supply a more specific standard.

## Product and usability
- Start from user intent: primary task, information needed, expected next action.
- Prioritize visible system status, clear affordances, predictable navigation and
  recoverable errors. Minimize unnecessary steps.
- Support screen-reader users, keyboard users, touch users, low-vision users and
  users with reduced-motion preferences.
- Avoid surprising destructive actions; label irreversible outcomes and require
  appropriate confirmation.
- Write concise UI copy that states what happened and what action to take.

## Visual system
- Establish one clear hierarchy per viewport: title/primary action/supporting content.
- Use a coherent type scale, line height, space scale, radii and elevation; apply
  existing design tokens instead of ad hoc values.
- Align related elements on a deliberate grid. Use whitespace to express grouping,
  not to hide content. Balance scanning density against task complexity.
- Prefer real product imagery, iconography and assets already in the repository;
  do not invent copyrighted brand marks or pretend placeholder images are real.
- Avoid gratuitous gradients, oversized hero cards, repetitive glowing borders
  and identical generic dashboards unless the product explicitly calls for them.
- Reuse components for repeated interactions and states; do not duplicate visual rules.
- Preserve the application's existing visual identity unless redesign is in scope.

## Responsive and native
- Design content-driven breakpoints, not just fixed device screenshots.
- No horizontal overflow at intended widths. Maintain touch targets,
  readable typography, safe-area insets, and sensible scrolling.
- Preserve logical reading/focus order when layout rearranges.
- Web: semantic HTML, responsive images, container behavior, reduced-motion.
- SwiftUI/macOS/iOS: native semantics, Dynamic Type when appropriate, adaptive
  layouts, keyboard interactions, focus and accessibility modifiers. Do not
  apply web idioms blindly to desktop applications.

## Required interaction inventory
Check states that actually exist for the feature:
default, hover (pointer), focus-visible, selected, disabled, pressed, loading,
empty, validation error, network error, success, and long-content/overflow.
Do not add fictitious interaction states just to complete a checklist.
Ensure feedback is specific, recoverable and persists appropriately.

## Accessibility baseline
- Use project target standard; if unspecified, aim for WCAG 2.2 AA for web.
- Validate accessible names, landmarks/headings, tab order and visible focus.
- Do not convey essential meaning by color alone. Check **actual**
  foreground/background colors before asserting contrast compliance.
- Standard text contrast target 4.5:1; large text target 3:1 where WCAG applies.
- Nontext UI boundaries/focus indicators should meet applicable contrast requirements.
- Forms: labels, helper/error association, field-level feedback, error summary when useful.
- Respect reduced motion. Avoid unexpected layout shifts and auto-playing effects.
- Automated axe/lighthouse checks are useful but do not replace keyboard and screen-reader review.

## Design anti-regression
- Prefer precise, localized changes over broad CSS overrides.
- Never sacrifice keyboard behavior, data correctness or error feedback for aesthetics.
- When reference screenshots conflict with the live product state, report the conflict
  and distinguish a visual preference from a behavioral requirement.
- Acceptance requires actual render inspection, not only subjective code review.
