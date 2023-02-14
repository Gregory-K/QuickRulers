import sublime
import sublime_plugin


def get_config():
    """Get Default/User Settings."""
    global DEFAULT_RULERS
    DEFAULT_RULERS = (
        sublime.load_settings("quick_rulers.sublime-settings")
        .get('default_rulers')
    )


def plugin_loaded():
    """Get config on load."""
    get_config()


def get_view_setting(view, sname, default=None):
    """Check if a setting is view-specific and only then return its value.
    | Otherwise return `default`.
    """
    s = view.settings()
    value = s.get(sname)
    s.erase(sname)
    value2 = s.get(sname)
    if value2 == value:
        return default
    s.set(sname, value)
    return value


def int_or_float(value):
    """Check value and Return int or float."""
    try:
        return int(value)
    except ValueError:
        return float(value)


class QuickRulersCommand(sublime_plugin.TextCommand):
    """Command that opens a quick panel to enter a list of ruler positions.
    | With live preview.
    """

    # "Instance" variables
    backup = None
    s = None

    def run(self, edit, show_current=True):
        self.backup = get_view_setting(self.view, "rulers")
        self.s = self.view.settings()


        if show_current is True and self.backup:
            default_text = ",".join(map(str, self.backup))
        elif show_current is False:
            default_text = ""
        else:
            default_text = DEFAULT_RULERS

        v = self.view.window().show_input_panel(
            "Position(s) of the ruler(s), separated by commas:",
            default_text,
            self.on_done,
            self.on_change,
            self.on_cancel
        )

        if default_text:
            # Select default text
            v.sel().clear()
            v.sel().add(sublime.Region(0, v.size()))

    def on_change(self, text, done=False):
        if text:
            try:
                rulers = [
                    int_or_float(r.strip()) for r in text.split(',') if r
                ]
            except ValueError as e:
                sublime.status_message(str(e))
                if done:
                    # Restore original stuff if invalid input and submitted
                    self.on_cancel()
                    return
            else:
                sublime.status_message('')
                rulers = sorted(set(rulers))  # remove duplicates and sort
                self.s.set("rulers", rulers)
                return

        # Format is wrong or empty, so erase all rulers to indicate that
        self.s.erase("rulers")

    def on_done(self, text):
        self.on_change(text, done=True)

    def on_cancel(self):
        if self.backup:
            self.s.set("rulers", self.backup)
        else:
            self.s.erase("rulers")
