# Zim Random Note

A third-party plugin for [Zim Desktop Wiki](https://zim-wiki.org/) that opens a random non-empty note from the current notebook.

### Features

The plugin adds the following command:

`Tools → Random Note`

When invoked, it selects a random page that has its own content and opens it in the current Zim window.

Empty namespace pages and pages without content are excluded from the selection.

### Installation

1. Copy the `randomnote` directory to the Zim user plugins directory.
2. Restart Zim and enable **Random Note** in: `Edit → Preferences → Plugins`.

The command will then be available from: `Tools → Random Note`

### Keyboard shortcut

The plugin does not assign a keyboard shortcut by itself. A shortcut can be configured separately using Zim's own key binding settings.

### What gets selected

The current version uses Zim's notebook index. A page is eligible when:

- its page file exists;
- it has its own content.

This means that normal note pages can be selected, while empty namespace/container pages are excluded.

### License

GNU General Public License v2.0 or later.
