from flask import render_template

class ImageHandler:
    def __init__(self, entries, default_entry, on_change):
        self.entries = entries
        self.default_entry = default_entry
        self.on_change = on_change

    def render(self):
        return render_template('image_handler.html', entries=self.entries, default_entry=self.default_entry)