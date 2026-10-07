# Zim Random Note

## Русский

Небольшой плагин для [Zim](https://zim-wiki.org/), который открывает случайную непустую заметку из текущего notebook.

### Возможности

Плагин добавляет команду:

`Tools → Random Note`

При вызове выбирается случайная страница, у которой есть собственное содержимое, и она открывается в текущем окне Zim.

Пустые страницы-каталоги и страницы без содержимого не выбираются.

### Установка

1. Скопируйте каталог `randomnote` в пользовательский каталог плагинов Zim.
2. Перезапустите Zim и включите плагин (Random Note) в `Edit → Preferences → Plugins`

После этого команда будет доступна в:

`Tools → Random Note`

### Горячие клавиши

Плагин не назначает горячую клавишу самостоятельно. Сочетание можно настроить отдельно средствами Zim.

### Что выбирается

В текущей версии используется индекс Zim. Выбираются страницы, для которых:

- существует файл страницы;
- страница имеет собственное содержимое.

Таким образом, обычные страницы заметок участвуют в случайном выборе, а пустые страницы-разделы — нет.

### Лицензия

GNU General Public License v2.0 or later.

---

## English

A small plugin for [Zim](https://zim-wiki.org/) that opens a random non-empty note from the current notebook.

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
