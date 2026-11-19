# Progressive contracts for design tasks

Only use the artifacts a task needs. XS/S tasks can use a short inline contract.
For M/L/XL, record a scoped, user-reviewable contract before broad edits.

## Design contract (M+)

```markdown
# DESIGN CONTRACT — <feature>
User goal:
Target audience and primary task:
Reference screen/design (or none):
Platform/framework:
Existing design-system source:
Non-goals:
Design direction:
Screen hierarchy / UX flow:
UI states in scope:
Viewports:
A11y requirements:
Functional invariants:
Owned files / single writer:
Read-only parallel agents needed (and why):
Acceptance criteria:
Test / render / screenshot commands:
Open questions (only blocking questions):
```

## Subagent task (one bounded unit)

```markdown
Task ID:
Agent/model/effort:
Objective:
Allowed WRITE files:
Read-only references:
Design constraints:
Explicit non-goals:
Done when:
Commands/evidence:
Stop/escalate if:
Return format: changed files, checks, screenshot, open issues
```

## Reviewer output

| Severity | Where (file/screen/state/viewport) | Observed evidence | User impact | Minimum fix | Verification |
|---|---|---|---|---|---|
| Critical | | | | | |
| Major | | | | | |
| Minor | | | | | |

A report may say `not verifiable` if no live screenshot or interactive preview was available.

## Read-only design concept comparison

| Concept | Layout and interaction direction | Expected user benefit | Accessibility risks | Evidence needed | Selected? |
|---|---|---|---|---|---|
| A | | | | | |
| B | | | | | |

Each concept is a **proposal**, not a concurrent edit to the same file.
Once a concept is selected, one active file owner implements it and records
actual test/render results. No version control is required.
