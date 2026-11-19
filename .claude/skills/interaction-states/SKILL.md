---
name: interaction-states
description: "Design interactive UX behavior for forms, buttons, dialogs, navigation, loading, validation, empty/error/success states, hover/focus, feedback and microinteractions. Use when user mentions interaction design, control states, form UX, modal flow, transitions, loading/error UX or confusing user feedback."
user-invocable: true
---

# Interaction design and state modeling

Inspect existing state management, domain events and user flows. Do not fabricate backend behavior.

1. List relevant user-triggered events and system-triggered events.
2. Define state machine/table: prior state, trigger, next state, feedback, errors/recovery and dismissal.
3. Specify keyboard behavior, focus placement/return, ARIA announcements or native accessibility equivalents.
4. Resolve double-submit, cancellation, optimistic update, retry, stale data and destructive action handling where relevant.
5. Set motion purpose and reduced-motion fallback; use existing transition system, not unneeded animation.
6. Include checks for disabled vs loading, validation, error feedback and recoverability.

**Output:** state/transition table, implementation constraints, test scenarios and accessibility notes.
**Boundary:** Keep UI behavior consistent with the real API/validation; assign code changes to one file owner.
