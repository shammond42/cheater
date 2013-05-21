import sublime, sublime_plugin
from os.path import dirname, realpath, join

MY_PLUGIN_DIR = dirname(realpath(__file__))

class RegExCheatSheetCommand(sublime_plugin.WindowCommand):
  def run(self):
    dest_view = self.window.open_file(join(MY_PLUGIN_DIR,'cheat_sheets/Regular Expressions.cheatsheet'))

    def set_view_props():
      if dest_view.is_loading():
        sublime.set_timeout(set_view_props, 50)
        return

      dest_view.set_name('RegEx Cheat Sheet')
      dest_view.set_syntax_file(join(MY_PLUGIN_DIR,'CheatSheet.tmLanguage'))
      dest_view.set_scratch(True)
      dest_view.set_read_only(True)

    set_view_props()
    self.dest_view = dest_view