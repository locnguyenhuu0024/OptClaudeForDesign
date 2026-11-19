---
name: ux-flow
description: "Design UX journeys, information architecture, navigation, wireframes, onboarding steps and user task flows. Use when a request mentions user journey, UX flow, IA, navigation structure, wireframe, task completion, funnel, or simplifying a multi-step experience. Not for color-only polish."
user-invocable: true
---

# UX flow and information architecture

Trigger only for **how users accomplish tasks**, not generic styling.
Read existing routes, screens, product requirements and observed behavior before proposing a new flow.

1. Define persona/actor only if supported by the brief; identify the job-to-be-done, entry, success and exit.
2. Map the **happy path**, alternate paths, error recovery, permission/empty states and system feedback. Keep steps few and transitions unambiguous.
3. Audit page hierarchy, labels, navigation destinations, action discoverability, back/escape behavior, destructive actions and forms.
4. Produce a compact screen/step table: current state -> user intent -> action -> next state -> success evidence.
5. Surface assumptions and trade-offs; do not pretend to have performed user research or usability studies.
6. Hand off implementation-ready interactions and acceptance tests to the orchestrator or writer.

**Output:** task goal; prioritized user flow; states/transitions; UX issues; measurable acceptance criteria.
**Boundary:** Do not modify source by default. Use `interaction-states` only if the task explicitly needs control behavior/state coverage.
