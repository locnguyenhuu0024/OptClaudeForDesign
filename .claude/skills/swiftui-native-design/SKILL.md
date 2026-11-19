---
name: swiftui-native-design
description: "Design native SwiftUI interfaces for macOS, iOS or iPadOS, including menus, window layout, keyboard shortcuts, native controls, sidebar navigation, Dynamic Type, VoiceOver and accessibility. Use when the UI project is SwiftUI or the request explicitly concerns a macOS/iOS native app. Not for React/HTML."
user-invocable: true
---

# Native SwiftUI UX/UI

Determine platform (macOS/iOS/iPadOS), deployment target, current navigation and Human Interface Guidelines expectations.
Prefer native affordances and project architecture over web-like replicas.

1. macOS: inspect sidebars/toolbars, menu commands, window resizability, focus/keyboard shortcuts, sheets/popovers and multi-window behavior.
2. iOS/iPadOS: inspect safe areas, Dynamic Type, navigation stacks/split views, touch targets, portrait/landscape and device adaptation.
3. Reuse environment values, semantic colors, SF Symbols where permitted and platform-appropriate feedback. Keep accessibility labels/actions meaningful.
4. Preserve SwiftUI state ownership and data flow; avoid moving domain logic into Views for polish.
5. Inspect light/dark appearance, empty/loading/error states, localization and long text; don't lock to preview-only mock data.
6. Build and run native preview/simulator/app if accessible; use screenshots plus interaction checks. Otherwise label runtime checks blocked.

**Output:** platform-specific design contract, view/component plan, actual verification results.
**Boundary:** Do not import unsupported frameworks or assume an iOS simulator/macOS GUI is available.
