import sublime, sublime_plugin

class RegExCheatSheetCommand(sublime_plugin.WindowCommand):
  def run(self):
    dest_view = self.window.open_file('cheat_sheets/Regular Expressions')

    dest_view.set_name('RegEx Cheat Sheet')
    dest_view.set_scratch(True)
    dest_view.set_read_only(True)

    self.dest_view = dest_view
