"""
Restructure patterns.json: convert guide/pitfalls from flat FR arrays
to {fr: [...], en: [...]} objects with English translations.
"""
import json, re

with open('src/_data/patterns.json', encoding='utf-8') as f:
    patterns = json.load(f)

# English translations for guide and pitfalls per slug
T = {
    'sidebar-collapsible-icon-rail': {
        'guide': [
            '**Width**: open state 200–260 px, collapsed 40–56 px. Never go below 40 px (click targets too small).',
            '**Transition**: `transition: width 200ms ease-in-out` is enough. Avoid animating label opacity separately — it delays readability.',
            '**Persistent state**: save open/closed in `localStorage` or server-side per user. Never reset on every visit.',
            '**Tooltip**: in collapsed mode, a hover tooltip is mandatory — use the HTML `title` attribute or a dedicated component with a 300 ms delay.',
            '**Sub-navigation**: in collapsed mode, sections with sub-menus open as flyouts (floating panel anchored to the icon), not as accordions.',
            '**Breakpoints**: on mobile the sidebar becomes a drawer (overlay) rather than an icon rail — the rail is a desktop-only pattern.',
        ],
        'pitfalls': [
            '❌ Hiding icons in collapsed mode — icons are the navigable element, not labels',
            '❌ Forgetting keyboard focus — Tab must traverse icons with a visible outline',
            '❌ Generic icons (star, dot) that lose meaning without labels — choose semantically strong icons',
            '❌ Triggering collapse on hover — causes accidental closures during mouse movements',
            '❌ Animating width AND opacity simultaneously — animation overload disrupts readability',
            '--',
        ],
    },
    'top-nav-contextual-left-panel': {
        'guide': [
            '**Strict hierarchy**: top nav = global sections (max 6–8 items), left panel = intra-section navigation. Never mix the two levels.',
            '**Top nav height**: 48–64 px. Below that, click targets are too small on desktop with an imprecise mouse.',
            '**Active indicator**: in the top nav the active item must be visually distinct (underline, background, color). In the left panel a background highlight is enough.',
            '**Left panel width**: 200–240 px fixed. Avoid resizable unless it is an explicit feature (e.g. file explorer).',
            '**Independent scroll**: the left panel must scroll independently of main content (`overflow-y: auto` on the panel).',
        ],
        'pitfalls': [
            '❌ Too many items in the top nav — beyond 7–8, use a "More" menu or rethink the IA',
            '❌ Left panel that disappears or changes on scroll — it must stay `position: sticky`',
            '❌ Duplicating navigation between top nav and left panel for the same level',
            '❌ Left panel with no clearly visible active state — the user loses orientation',
            '--',
        ],
    },
    'breadcrumb-dynamique': {
        'guide': [
            '**Separator**: use `›` or `/`, avoid `>` (too aggressive). A subtle color on the separator reduces visual noise.',
            '**Last item**: non-clickable and slightly bolder or differently colored to signal "current location".',
            '**Long paths**: truncate the middle section (home › … › parent › current) rather than the beginning or end.',
            '**Dynamic update**: on SPA navigation update the breadcrumb without a full reload — use history events or a routing hook.',
            '**Structured data**: add `JSON-LD BreadcrumbList` schema to every page for Google rich results.',
        ],
        'pitfalls': [
            '❌ Showing the breadcrumb on the home page (it adds nothing there)',
            '❌ Truncating the last segment — the user must always see where they are',
            '❌ A breadcrumb that lags behind the URL (SPA routing update missed)',
            '❌ Using the breadcrumb as the sole navigation — it complements, it does not replace the menu',
        ],
    },
    'tabs-persistants-pinnable': {
        'guide': [
            '**Persistence**: save the open tab list in `localStorage` (order, pinned state, scroll position per tab).',
            '**Maximum**: beyond 10–12 tabs, offer a search or "recently closed" panel. Avoid horizontal scroll — prefer a dropdown overflow.',
            '**Pinning**: pinned tabs lose their label and are displayed as a compact icon-only tab at the start of the row.',
            '**Close gesture**: middle-click to close is standard on the web — support it with `pointerdown` + `button === 1`.',
            '**Visual indication**: active tab = strong contrast; pinned tab = small lock or pin icon.',
        ],
        'pitfalls': [
            '❌ Tabs that close on accidental click — always require explicit close (× button, not the tab itself)',
            '❌ Unlimited pinned tabs — cap at 5–6 to avoid a cluttered rail',
            '❌ Tab state lost on refresh — persistence is the whole point of the pattern',
            '❌ No visual distinction between pinned and regular tabs',
        ],
    },
    'right-panel-contextuel-d-tail': {
        'guide': [
            '**Width**: 320–480 px on desktop. On tablet use a full-screen modal instead.',
            '**Animation**: slide in from the right (`translateX(100%)` → `0`) in 200 ms — fast enough not to feel sluggish.',
            '**Keyboard shortcut**: `Escape` closes the panel; `F` (or a dedicated shortcut) focuses the panel.',
            '**Content area**: the main content area shrinks to accommodate the panel (push layout), or the panel overlays it — push is preferable to avoid content jumping.',
            '**Loading state**: show a skeleton immediately while the content loads, not a blank panel.',
        ],
        'pitfalls': [
            '❌ A panel that opens full-screen on desktop — reserve full-screen for mobile',
            '❌ Not restoring the previous scroll position when the panel is closed',
            '❌ Panel content that reloads on every open — cache it',
            '❌ No accessible close button visible without scrolling',
        ],
    },
    'split-view-panneau-dual': {
        'guide': [
            '**Resize handle**: 4–8 px wide, cursor `col-resize` or `row-resize`. Show a visual drag indicator on hover.',
            '**Minimum sizes**: each pane should have a minimum width/height (e.g. 20%) to prevent accidental full collapse.',
            '**Persistence**: save pane sizes in `localStorage` so they survive a refresh.',
            '**Keyboard resize**: support `Alt+Arrow` to resize with the keyboard for accessibility.',
            '**Overflow**: each pane scrolls independently — `overflow: auto` on each pane container.',
        ],
        'pitfalls': [
            '❌ A resize handle too thin to click reliably (< 4 px)',
            '❌ Panes with no minimum size — one pane can be crushed to 0',
            '❌ Resizing that causes layout reflow in both panes simultaneously — causes jitter',
            '❌ Forgetting keyboard users — always add keyboard resize support',
        ],
    },
    'floating-action-button-fab': {
        'guide': [
            '**Position**: bottom-right corner, 16–24 px from edges. On mobile keep it above the bottom nav bar.',
            '**Size**: primary FAB 56 px, mini FAB 40 px. Never go below 40 px.',
            '**Actions**: expand to max 5 sub-actions. Beyond that, use a modal sheet instead.',
            '**Label**: add a text label to the right of the FAB in contexts where the icon alone is ambiguous.',
            '**Scroll hide**: hide the FAB when the user scrolls down a content list to avoid obscuring items.',
        ],
        'pitfalls': [
            '❌ More than one primary FAB per screen — it becomes unclear what the main action is',
            '❌ A FAB that covers important content and cannot be dismissed',
            '❌ Using a FAB for destructive actions (delete, logout) — reserve it for creation/positive actions',
            '❌ No keyboard access to the FAB sub-actions',
        ],
    },
    'board-vue-switcher': {
        'guide': [
            '**Persistence**: save the active view in `localStorage` so the user always returns to their preferred view.',
            '**Seamless transition**: switching views should not reload the data — just re-render the same dataset with a different component.',
            '**Icons + labels**: use both icon and label in the switcher — icon alone is often ambiguous between Board and Table.',
            '**Mobile default**: on small screens default to List view — Board (Kanban) and Table require too much horizontal space.',
            '**URL param**: encode the active view in the URL (`?view=board`) so links can target a specific view.',
        ],
        'pitfalls': [
            '❌ Reloading data on every view switch — cache and reuse the fetched dataset',
            '❌ A view switcher that appears in a different position depending on the view',
            '❌ Not persisting the active view — the user must re-select it on every visit',
        ],
    },
    'command-palette-k': {
        'guide': [
            '**Trigger**: `Cmd/Ctrl+K` is the universal shortcut. Show it visually in the search trigger button in the header.',
            '**Fuzzy search**: use a library like Fuse.js for fuzzy matching — exact prefix matching feels too rigid.',
            '**Keyboard nav**: `↑↓` to select, `Enter` to execute, `Escape` to close. Auto-select the first result on open.',
            '**Grouping**: if results span multiple types (pages, actions, files), show group headers inside the palette.',
            '**Recent items**: show the 5 most recently visited items by default when the query is empty.',
        ],
        'pitfalls': [
            '❌ Opening the palette but not auto-focusing the input',
            '❌ Showing more than 8 results at once — overwhelming and hard to scan',
            '❌ No empty state message when no results are found',
            '❌ Command palette that only searches routes but not actions (e.g. "toggle dark mode")',
        ],
    },
    'omnibox-unified-search': {
        'guide': [
            '**Debounce**: wait 150–200 ms after the last keystroke before querying the server — avoid hammering the API.',
            '**Grouped results**: show results in named categories (People, Files, Pages) with clear visual separation.',
            '**Keyboard nav**: arrow keys navigate within and across groups. `Tab` moves to next group.',
            '**Loading state**: show a spinner or skeleton in the results area while the query is in flight.',
            '**Recent + suggested**: pre-populate with recent searches and suggested items before the user types.',
        ],
        'pitfalls': [
            '❌ Mixing all result types in a flat list — grouping is essential for scanability',
            '❌ A minimum of 3 characters before searching — 1 character is the right threshold for most datasets',
            '❌ Results that load in one big batch — stream partial results as they arrive',
            '❌ Forgetting to highlight the matched portion of each result',
        ],
    },
    'inline-slash-commands': {
        'guide': [
            '**Trigger**: `/` at the start of a new line or after a space. Do not trigger mid-word.',
            '**Menu position**: anchor the menu below the cursor position, with screen-edge detection to flip upward when near the bottom.',
            '**Fuzzy filter**: filter the command list as the user types after `/` — supports both `/h` → heading and `/heading`.',
            '**Keyboard nav**: `↑↓` to navigate, `Enter` to execute, `Escape` to cancel (and leave the typed `/` in place).',
            '**Categories**: group commands by type (Text, Media, Embed, AI) with visual dividers.',
        ],
        'pitfalls': [
            '❌ Triggering the menu when the user types `/` in the middle of a URL',
            '❌ A command menu that cannot be dismissed with Escape',
            '❌ Not supporting keyboard navigation — mouse-only menus are inaccessible',
            '❌ Commands that insert content without showing a preview or undo option',
        ],
    },
    'contextual-right-click-menu': {
        'guide': [
            '**Position**: open at cursor position; flip left if it would overflow the right edge, flip up if it would overflow the bottom.',
            '**Content**: show only contextually relevant actions — a context menu on a file should differ from one on an empty area.',
            '**Keyboard trigger**: `Shift+F10` or `Menu key` must also open the context menu for accessibility.',
            '**Dismiss**: click outside, `Escape`, or any action closes it. Navigating focus out should also close it.',
            '**Icons**: icons in context menus are optional but improve scannability — keep them consistent across the app.',
        ],
        'pitfalls': [
            '❌ Context menus with more than 10 items — split into a submenu or remove rarely used items',
            '❌ Using the browser default context menu for content the user might want to copy — respect native behavior',
            '❌ A context menu that appears behind other content (z-index issues)',
            '❌ No keyboard trigger support',
        ],
    },
    'spreadsheet-like-inline-editing': {
        'guide': [
            '**Trigger**: single click selects the cell; double-click enters edit mode. This matches the Excel/Sheets mental model.',
            '**Confirm/cancel**: `Enter` or `Tab` confirms and moves focus; `Escape` cancels and reverts the value.',
            '**Validation**: show inline validation errors below the cell while editing — not a toast.',
            '**Optimistic update**: update the UI immediately on confirm; roll back silently if the server returns an error.',
            '**Keyboard navigation**: `Tab` moves to the next editable cell; `Shift+Tab` moves back; arrow keys navigate the grid in view mode.',
        ],
        'pitfalls': [
            '❌ Forcing a click on a separate "Edit" button per row — too many clicks for frequent editing',
            '❌ Saving on every keystroke — debounce or save on blur/Enter only',
            '❌ No visual distinction between editable and read-only cells',
            '❌ Validation that only fires on server round-trip — too slow for inline editing',
        ],
    },
    'filtres-persistants-url-encod-s': {
        'guide': [
            '**URL encoding**: serialize all active filters in the URL query string so the filtered view is shareable and bookmarkable.',
            '**Filter chips**: each active filter displays as a removable chip with the filter name and value. `×` to remove individually.',
            '**"Clear all"**: always offer a single "Clear all filters" button when at least one filter is active.',
            '**Filter count**: show the number of active filters in the filter button label ("Filters · 3").',
            '**Persistence on navigation**: preserve filters when the user navigates to a detail page and returns (use the URL or browser history state).',
        ],
        'pitfalls': [
            '❌ Filters that reset when the user refreshes or navigates back',
            '❌ No visual indication that filters are active — users forget what they applied',
            '❌ Filters that require a "Submit" button — apply changes instantly for a responsive feel',
            '❌ URL with non-human-readable filter encoding — prefer `?status=open&priority=high` over base64 blobs',
        ],
    },
    'virtual-scrolling': {
        'guide': [
            '**When to use**: virtual scrolling pays off above ~500 DOM nodes. Below that, the complexity cost exceeds the performance gain.',
            '**Item height**: fixed item height is simpler (calculate rendered range from scroll position). Variable height requires a size cache.',
            '**Overscan**: render 3–5 items above and below the visible area to prevent blank flashes during fast scrolling.',
            '**Scroll restoration**: save the scroll offset in history state or session storage; restore it on back-navigation.',
            '**Accessible**: ensure screen readers can announce list items correctly — some virtual scroll libraries break ARIA roles.',
        ],
        'pitfalls': [
            '❌ Using virtual scrolling for lists of < 200 items — the complexity is not justified',
            '❌ Missing overscan — causes blank areas when scrolling quickly',
            '❌ Breaking CMD+F (browser find) — virtualized lists hide non-rendered nodes from the browser search',
            '❌ Forgetting scroll restoration — users lose their position when returning from a detail view',
        ],
    },
    'column-resizing-reordering': {
        'guide': [
            '**Resize handle**: a 4–8 px zone on the right edge of each header cell. Cursor changes to `col-resize` on hover.',
            '**Minimum column width**: set a floor (e.g. 60 px) so a column cannot be resized below readable size.',
            '**Persist**: save column widths and order in `localStorage` keyed by the table identifier.',
            '**Drag-to-reorder**: use a drag handle (⠿ icon) in the header, not the full header, to avoid conflict with column sorting.',
            '**Overflow columns**: if columns overflow the container, show a horizontal scroll on the table — do not hide columns silently.',
        ],
        'pitfalls': [
            '❌ Resize handles that are invisible until hover — provide at least a subtle visual hint',
            '❌ Resize that changes the layout of other columns unexpectedly (table-layout: fixed solves this)',
            '❌ No persistence — users must re-configure on every visit',
            '❌ Drag-to-reorder that also triggers a sort — separate the two interactions clearly',
        ],
    },
    'toast-notification-undo': {
        'guide': [
            '**Duration**: 4–6 seconds for informational toasts; 8–10 seconds for toasts with an undo action.',
            '**Undo**: the undo action must be instantly reversible — do the destructive action server-side only when the toast disappears.',
            '**Stack**: show a maximum of 3 toasts at once. Queue additional ones and show them in sequence.',
            '**Position**: bottom-right (desktop), bottom-center (mobile). Avoid top-right — it competes with system notifications.',
            '**Pause on hover**: pause the auto-dismiss timer while the user hovers over the toast.',
        ],
        'pitfalls': [
            '❌ A toast with no undo for a destructive action (delete, archive) — always offer undo for irreversible actions',
            '❌ Toasts that stack without a queue limit — can pile up and obscure content',
            '❌ An undo button that does a server round-trip before undoing the UI — feel the undo immediately',
            '❌ Toasts that disappear before the user can click Undo (< 4 s)',
        ],
    },
    'optimistic-ui': {
        'guide': [
            '**Apply immediately**: update the UI synchronously on user action, before the server responds.',
            '**Rollback on error**: if the server returns an error, revert the UI to its previous state and show an error toast.',
            '**Loading indicator**: show a subtle indicator (spinner, opacity change) to signal that the action is in flight.',
            '**Idempotent actions**: optimistic UI is safest for idempotent actions (toggle, update). For non-idempotent actions (payment, send email) show an explicit confirmation.',
            '**Conflict detection**: if a concurrent update from another user changes the same resource, show a conflict notification rather than silently overwriting.',
        ],
        'pitfalls': [
            '❌ Applying optimistic updates to non-reversible, high-stakes actions (payment, destructive delete)',
            '❌ No visual feedback that an update is pending — looks like the action was ignored',
            '❌ Silent rollback — always inform the user when an optimistic update failed',
            '❌ Race conditions when the user triggers the same action multiple times quickly — debounce or disable the action while pending',
        ],
    },
    'empty-states-actionnables': {
        'guide': [
            '**Context-specific**: tailor the empty state to the feature (empty inbox ≠ empty project). Generic "No data" messages waste an opportunity.',
            '**Primary CTA**: one clear action that directly addresses the emptiness ("Create your first project", "Invite a teammate").',
            '**Illustration**: a small, relevant illustration increases emotional appeal — but keep it simple and do not use it for error states.',
            '**Educational content**: the empty state is a prime spot to explain the value of the feature ("Projects help you group tasks by client").',
            '**Filter reset**: if the empty state is caused by an active filter, show a "Clear filters" button instead of a creation CTA.',
        ],
        'pitfalls': [
            '❌ Generic "No results found" without any guidance',
            '❌ An empty state that looks like an error — make it feel intentional and welcoming',
            '❌ A CTA that navigates away from the current page — the user should complete the action without losing context',
            '❌ No empty state at all — a blank white area is disorienting',
        ],
    },
    'skeleton-screens': {
        'guide': [
            '**Shape matching**: skeleton blocks must match the exact shape of the final content (width, height, border-radius) — mismatched skeletons cause layout shift on load.',
            '**Animation**: a left-to-right shimmer (`@keyframes shimmer`) is the standard. Use `animation-duration: 1.5 s` for a natural feel.',
            '**Progressive reveal**: fade out skeleton and fade in real content, not a hard swap — reduces perceived load time.',
            '**Timeout**: if content takes > 10 s to load, replace the skeleton with an error state — do not leave a skeleton indefinitely.',
            '**Not for errors**: skeleton screens communicate "loading", not "failed" — switch to an error state if the request fails.',
        ],
        'pitfalls': [
            '❌ Skeletons that do not match the layout of the real content — causes jarring layout shift',
            '❌ Using a spinner instead of skeletons for large content areas — skeletons feel faster',
            '❌ Skeleton left visible after an error — no content will ever appear',
            '❌ Overly complex skeletons that take longer to render than the real content',
        ],
    },
    'ai-sidebar-persistante': {
        'guide': [
            '**Persistent context**: the AI sidebar should maintain conversation history for the session so the user can refer back to earlier exchanges.',
            '**Context injection**: automatically inject the current page/item context into every query ("You are looking at Invoice #1234, created on...").',
            '**Width**: 320–400 px on desktop. On tablet use a sheet/drawer. On mobile use a full-screen modal.',
            '**Streaming responses**: stream the AI response token by token rather than showing a loading state then the full answer.',
            '**Input height**: the input should auto-grow up to 3–4 lines; beyond that add a scrollbar.',
        ],
        'pitfalls': [
            '❌ A sidebar that resets its history when the user navigates — persistence is the core value proposition',
            '❌ No context injection — AI responses that ignore the current page are unhelpful',
            '❌ Blocking the main content with the sidebar — it should overlay or push; user must be able to interact with both',
            '❌ No way to clear the conversation history',
        ],
    },
    'k-ai-intent': {
        'guide': [
            '**Intent detection**: if the query is a question or a sentence (not a command name), route it to the AI instead of the command list.',
            '**Visual distinction**: show an "Ask AI" option at the top of results with a distinctive icon (✦, ✱, or a model logo).',
            '**Progressive disclosure**: open the AI response inline in the palette or navigate to a dedicated chat view, depending on answer length.',
            '**Hybrid results**: show matching commands alongside the AI option — do not hide commands when AI is active.',
            '**History**: save recent AI queries in the command palette "recents" list.',
        ],
        'pitfalls': [
            '❌ Triggering AI for every query including exact command matches — show AI option only when no exact match exists',
            '❌ Making the AI option indistinguishable from regular commands — it must stand out visually',
            '❌ AI that responds with a wall of text inside the palette — summarize and offer "See full answer"',
        ],
    },
    'floating-ai-button-contextuel': {
        'guide': [
            '**Trigger**: appear on text selection (debounced 200 ms) and on right-click. Disappear on scroll or outside click.',
            '**Position**: anchor to the selection end, not the start. Detect viewport edges and flip accordingly.',
            '**Actions**: offer 3–5 focused actions (Explain, Rewrite, Translate, Summarize, Fix). More = decision fatigue.',
            '**Inline result**: show the AI response inline near the selection rather than navigating away.',
            '**Undo**: always offer an Undo after an AI edit is applied to the document.',
        ],
        'pitfalls': [
            '❌ Button that appears on every single click, not just on text selection',
            '❌ Button that blocks the selected text from being read',
            '❌ No way to dismiss the button with the keyboard (Escape)',
            '❌ AI edits applied without confirmation for long or complex replacements',
        ],
    },
    'inline-slash-ai-commands': {
        'guide': [
            '**Trigger**: `/ai` as a dedicated prefix, or integrate AI commands into the general `/` menu under an "AI" group.',
            '**Context awareness**: pass the surrounding paragraph text as context when executing the command.',
            '**Preview before insert**: show a diff preview of what will be inserted/replaced before confirming.',
            '**Streaming insert**: stream the AI-generated content into the document character by character.',
            '**Undo**: always make the AI insertion reversible with a single `Cmd+Z`.',
        ],
        'pitfalls': [
            '❌ AI commands that replace content without showing a preview',
            '❌ Not passing surrounding context — AI suggestions that are generic and not adapted to the document',
            '❌ Streaming insertion that cannot be stopped mid-stream',
            '❌ No error handling when the AI call fails — the user is left with a partial insert',
        ],
    },
    'streaming-text-typewriter': {
        'guide': [
            '**SSE or WebSocket**: use Server-Sent Events (`EventSource`) for one-way streaming, WebSocket for bidirectional.',
            '**Chunk rendering**: append each incoming token to the DOM immediately — do not buffer before rendering.',
            '**Cursor**: show a blinking cursor at the end of the streamed text while generation is in progress.',
            '**Scroll lock**: auto-scroll to the bottom of the response area as new tokens arrive, unless the user has manually scrolled up.',
            '**Stop button**: always offer a way to stop generation mid-stream.',
        ],
        'pitfalls': [
            '❌ Blocking the UI while waiting for the full response — streaming is the fix for this',
            '❌ Flickering caused by re-rendering the entire text on each token — append, do not replace',
            '❌ No stop button — trapped users will simply close the page',
            '❌ Streaming that stops abruptly without a final state indicator (done/error)',
        ],
    },
    'diff-view-accept-reject': {
        'guide': [
            '**Inline diff**: show added lines in green, removed in red, unchanged in neutral. Use a word-level diff for short changes.',
            '**Per-hunk controls**: each diff hunk (block of related changes) should have its own Accept/Reject button.',
            '**"Accept all" / "Reject all"**: provide bulk controls in the toolbar above the diff.',
            '**Undo**: accepting or rejecting a change should be undoable in the document history.',
            '**Context lines**: show 2–3 unchanged context lines above and below each hunk to help the user understand the change.',
        ],
        'pitfalls': [
            '❌ Showing a diff without context lines — isolated changes are hard to evaluate',
            '❌ No per-hunk controls — forcing the user to accept or reject everything at once',
            '❌ A diff view that is read-only (no accept/reject) — it is then just documentation, not a workflow',
            '❌ Word-wrap differences making the diff hard to read — always use a monospace font',
        ],
    },
    'ghost-text-inline-autocomplete': {
        'guide': [
            '**Trigger**: show ghost text after a typing pause of 300–500 ms. Do not show on every keystroke — too distracting.',
            '**Accept**: `Tab` accepts the full suggestion. `→` (right arrow) accepts word by word.',
            '**Dismiss**: any other keypress dismisses the ghost text without affecting the typed content.',
            '**Contrast**: use `color: rgba(text, 0.35)` for the ghost text — visible but clearly distinct from typed text.',
            '**Context**: send the full current input (or last paragraph) as context for the completion, not just the last word.',
        ],
        'pitfalls': [
            '❌ Ghost text that overlaps the cursor position — it must always start after the last typed character',
            '❌ Suggestions that are too long (> 1 sentence) — short, high-confidence completions work best',
            '❌ No dismiss mechanism — the ghost text should not be permanent',
            '❌ Triggering completion on every keystroke — too noisy and burns API credits',
        ],
    },
    'canvas-artifact-panel': {
        'guide': [
            '**Split layout**: code/source on the left, rendered output on the right. Draggable divider between the two.',
            '**Auto-update**: re-render the preview as the user types (debounced 300 ms) — not just on save.',
            '**Artifact types**: support code (syntax-highlighted), Markdown (rendered), HTML/React (iframe preview), and images.',
            '**Version history**: save previous artifact versions so the user can navigate back through the conversation.',
            '**Export**: provide a copy/download button on the artifact panel for the raw content.',
        ],
        'pitfalls': [
            '❌ A preview that only updates on explicit save — breaks the live feedback loop',
            '❌ Rendering untrusted HTML in the same origin — always use a sandboxed iframe for HTML artifacts',
            '❌ No syntax highlighting in the code view — even a simple highlight improves readability',
            '❌ Artifact panel that cannot be resized or maximized — some artifacts need more space',
        ],
    },
    'mentions-pour-le-contexte': {
        'guide': [
            '**Trigger**: `@` character, optionally followed by search text. Show the picker after a brief delay (100 ms).',
            '**Search**: fuzzy search on name, username, and role. Rank by recency of collaboration.',
            '**Mentionable types**: people, teams, documents, issues — each with a distinct visual style in the picker.',
            '**Insertion**: replace the `@text` with a styled mention tag that is non-editable (treated as an atomic token).',
            '**Notification**: send a notification to the mentioned entity when the message is sent.',
        ],
        'pitfalls': [
            '❌ A mention picker with no search — forces the user to scroll through all users',
            '❌ Mentions that are plain text — once typed they cannot be corrected without retyping',
            '❌ No keyboard navigation in the picker — mouse-only is inaccessible',
            '❌ No avatar or team badge — makes it hard to distinguish people from documents in the list',
        ],
    },
    'fil-de-conversation-persistant': {
        'guide': [
            '**Persistence**: store the conversation server-side keyed to the user + context (not just in memory).',
            '**Resumption**: when the user reopens the context (page, document, object), restore the last conversation automatically.',
            '**Thread branching**: allow the user to start a new thread without losing the existing one.',
            '**Context summary**: after ~20 messages, show a collapsible summary of earlier conversation to keep the thread readable.',
            '**Export**: allow the user to export the full thread as Markdown or PDF.',
        ],
        'pitfalls': [
            '❌ Conversation that resets on page reload — defeats the purpose of persistence',
            '❌ No "start new conversation" option — users should not be trapped in a long thread',
            '❌ No timestamp on messages — makes it hard to understand when decisions were made',
            '❌ Thread that grows without a way to collapse older messages',
        ],
    },
    'memory-pr-f-rences-utilisateur': {
        'guide': [
            '**Explicit + implicit**: allow both explicit memory saves ("Remember that I prefer dark mode") and implicit ones learned from behavior.',
            '**Visibility**: show the user a list of all stored memories so they understand what the AI knows about them.',
            '**Edit/delete**: allow the user to edit or delete individual memories.',
            '**Context injection**: prepend relevant memories to every AI prompt as a system message, not as user messages.',
            '**Scoped vs global**: distinguish between app-wide preferences and project-specific memory.',
        ],
        'pitfalls': [
            '❌ Hidden memory — users must always be able to see what is stored about them',
            '❌ Unlimited memory growth — implement a soft cap and a "clear all" option',
            '❌ Injecting all memories into every prompt — select only relevant memories for each context',
            '❌ Memory that is not portable — consider allowing export/import',
        ],
    },
    'sources-cit-es-grounding': {
        'guide': [
            '**Inline markers**: number citations `[1]`, `[2]` inline in the text, at the sentence or claim level.',
            '**Reference list**: always show the full list of sources at the bottom of the response with title, URL, and access date.',
            '**Hover preview**: on hover over a citation marker, show a popover with the source title and snippet.',
            '**Truthfulness**: only cite real, checkable sources. If a source cannot be verified, omit the citation.',
            '**Highlight in source**: where possible, link directly to the specific paragraph in the source document (anchor link or highlight fragment).',
        ],
        'pitfalls': [
            '❌ Hallucinated citations — fabricated sources are worse than no citations',
            '❌ Citing sources that do not support the claim — citation mismatch erodes trust',
            '❌ Citation markers without a reference list — the user cannot check the source',
            '❌ Dead links — validate source URLs before including them',
        ],
    },
    'thinking-reasoning-visible': {
        'guide': [
            '**Collapsible**: the thinking section is collapsed by default, with a "Thinking…" / "View reasoning" toggle.',
            '**Visual distinction**: use a different background (subtle grey/purple tint) for the thinking block vs the final answer.',
            '**Stream the thinking**: if possible, stream the thinking tokens alongside the final answer — it builds trust in real-time.',
            '**Summary header**: display a one-line summary of what the model is thinking about ("Checking arithmetic…", "Searching for relevant context…").',
            '**Not for every response**: only show visible thinking for complex, multi-step tasks where the reasoning adds value.',
        ],
        'pitfalls': [
            '❌ Thinking block that is always expanded — it adds noise for simple queries',
            '❌ Showing raw token output without formatting — thinking is only useful when readable',
            '❌ Using thinking blocks to hide uncertainty — show uncertainty signals separately',
            '❌ Thinking that contradicts the final answer without explanation',
        ],
    },
    'regenerate-variantes': {
        'guide': [
            '**Variant axes**: offer variants along meaningful axes: tone (formal/casual), length (shorter/longer), style (technical/plain).',
            '**Preview**: show a short preview of each variant before the user selects one.',
            '**In-place replacement**: selecting a variant replaces the current response in the thread, not creates a new message.',
            '**History**: allow the user to navigate back to the original response and previous variants.',
            '**Keyboard shortcut**: `Cmd+Shift+R` to regenerate the last response.',
        ],
        'pitfalls': [
            '❌ Regenerating with the same parameters — variants must meaningfully differ from each other',
            '❌ More than 4 variants at once — choice overload',
            '❌ No way to return to the original if the variant is worse',
            '❌ Variants that reload the full page or conversation instead of replacing just the response',
        ],
    },
    'agentic-step-tracker': {
        'guide': [
            '**Step names**: use plain-language step names ("Searching the web", "Reading documents") not internal code names.',
            '**Current step indicator**: highlight the in-progress step with a spinner and a subtle animated color.',
            '**Collapsible**: allow the user to collapse the step tracker to a single-line summary.',
            '**Error state**: if a step fails, show it in red with a retry button and a plain-language error message.',
            '**Estimated time**: where possible, show an estimated duration per step (useful for long-running agents).',
        ],
        'pitfalls': [
            '❌ Step tracker that disappears when the task is complete — it is useful to review what happened',
            '❌ Steps that are too granular (> 10 steps) — group related micro-steps into higher-level steps',
            '❌ No error recovery — a failed step should offer retry, not just show a red cross',
            '❌ Steps described in technical jargon the user does not understand',
        ],
    },
    'confidence-uncertainty-signal': {
        'guide': [
            '**Calibration**: only show high confidence when the model is truly confident. Under-confident responses destroy trust as much as hallucinations.',
            '**Visual encoding**: use color (green/yellow/red), a bar, or a label — never rely on a single signal alone.',
            '**Explain uncertainty**: when confidence is low, briefly state why ("This is based on limited data" or "I may be wrong about the date").',
            '**Threshold**: only show the confidence signal when it is relevant — do not display it for every single sentence.',
            '**Actionable**: low confidence should trigger an action suggestion ("Please verify this with an official source").',
        ],
        'pitfalls': [
            '❌ Showing "100% confident" — no model is ever 100% confident on factual claims',
            '❌ Confidence signals that are decorative but not calibrated to actual model output',
            '❌ Low confidence without explanation — the signal is useless without context',
            '❌ Confidence bar that is always in the same color — variance is what makes it informative',
        ],
    },
    'suggested-prompts-quick-actions': {
        'guide': [
            '**Context-aware**: show prompts relevant to the current context — not generic ones. A project view should suggest "Summarize this project", not "Tell me a joke".',
            '**Refresh**: rotate suggestions after each response so they do not stale.',
            '**Max 4**: limit to 4 suggestions to avoid choice overload. Fewer is better.',
            '**Editable after insert**: when the user clicks a suggestion, it fills the input as editable text — not as a locked chip.',
            '**Learn from history**: weight suggestions toward topics the user has queried before.',
        ],
        'pitfalls': [
            '❌ Generic, non-contextual suggestions ("How can I help you today?")',
            '❌ Suggestions that are too long — they should be short enough to read at a glance',
            '❌ Locked chips that cannot be edited before sending',
            '❌ Suggestions that never change across sessions',
        ],
    },
    'prompt-templates': {
        'guide': [
            '**Variable slots**: templates must have editable variable slots (highlighted placeholders) so the user can fill in specific values.',
            '**Categories**: organize templates by use case (Writing, Analysis, Code, Research) with icons.',
            '**Search**: provide a search bar to find templates by name or category.',
            '**User templates**: allow users to save and name their own templates.',
            '**One-click insert**: clicking a template fills the input immediately — no intermediate step.',
        ],
        'pitfalls': [
            '❌ Templates with no variable placeholders — they are just boilerplate text the user must fully rewrite',
            '❌ Templates that are too long to read at a glance in the picker',
            '❌ No categorization — a flat list of 30+ templates is impossible to browse',
            '❌ Templates that cannot be edited or deleted by the user',
        ],
    },
    'multimodal-drop-zone': {
        'guide': [
            '**Visual affordance**: the drop zone should look like a drop zone — dashed border, upload icon, and hint text.',
            '**Drag highlight**: change the border color and background on `dragover` to confirm the drop target is active.',
            '**File type validation**: validate file type and size on the client before uploading. Show a clear error for unsupported types.',
            '**Progress**: for large files, show an upload progress bar per file.',
            '**Multiple files**: support multi-file upload — show each file as a preview card in the drop zone.',
        ],
        'pitfalls': [
            '❌ A drop zone that accepts any file type silently — then rejects it on the server',
            '❌ No progress feedback for uploads — the user cannot tell if anything is happening',
            '❌ Drop zone that covers the full screen on drag-enter — it should only highlight the relevant zone',
            '❌ No click-to-browse fallback for users who do not know about drag-and-drop',
        ],
    },
    'mode-voix-natif': {
        'guide': [
            '**Permission prompt**: request microphone permission only when the user explicitly activates voice mode — not on page load.',
            '**Waveform**: show a live audio waveform to confirm the microphone is active and picking up sound.',
            '**Transcript**: display the live transcript as the user speaks so they can monitor speech recognition accuracy.',
            '**Push-to-talk option**: offer both "always listening" and "push-to-talk" modes — PTT is preferred in noisy environments.',
            '**Wake word**: for ambient voice mode, support a configurable wake word so the mic is not always transmitting.',
        ],
        'pitfalls': [
            '❌ No visual feedback that the microphone is active — users cannot tell if they are being heard',
            '❌ Microphone that stays on after the user has finished speaking — always provide a clear off switch',
            '❌ No transcript — users cannot correct misrecognitions',
            '❌ Voice input that does not work without network connectivity — local speech recognition is preferable for short commands',
        ],
    },
}

# Apply transformations
updated = 0
for p in patterns:
    slug = p['slug']
    if slug in T:
        t = T[slug]
        p['guide'] = {'fr': p.get('guide', []), 'en': t['guide']}
        p['pitfalls'] = {'fr': p.get('pitfalls', []), 'en': t['pitfalls']}
        updated += 1
    else:
        # Keep FR, copy to EN as fallback
        p['guide'] = {'fr': p.get('guide', []), 'en': p.get('guide', [])}
        p['pitfalls'] = {'fr': p.get('pitfalls', []), 'en': p.get('pitfalls', [])}

with open('src/_data/patterns.json', 'w', encoding='utf-8') as f:
    json.dump(patterns, f, ensure_ascii=False, indent=2)

print(f'Done: {updated}/{len(patterns)} patterns with EN translations.')
