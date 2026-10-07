# -*- coding: utf-8 -*-

import random

from zim.plugins import PluginClass
from zim.actions import action
from zim.gui.mainwindow import MainWindowExtension


class RandomNotePlugin(PluginClass):
    plugin_info = {
        'name': _('Random Note'),
        'description': _('Open a random note from the current notebook'),
        'author': 'Pustolaika',
    }


class RandomNoteMainWindowExtension(MainWindowExtension):
    @action(
        _('Random Note'),
        menuhints='tools',
    )
    def random_note(self):
        notebook = self.window.notebook

        pages = [
            page
            for page in notebook.pages.walk()
            if page.hascontent and page.exists()
        ]

        if not pages:
            return

        page = random.choice(pages)
        self.window.open_page(page)
