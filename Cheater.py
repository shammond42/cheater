from os.path import dirname, exists, join, realpath
import sublime, sublime_plugin
import string

MY_PLUGIN_DIR = dirname(realpath(__file__))

class CheatSheetCommand(sublime_plugin.WindowCommand):
  def run(self, **args):
    sheetName = args["cheatsheet"] + ".cheatsheet"
    userSheet = join(sublime.packages_path(), "User/cheat_sheets", sheetName)
    defaultSheet = join(MY_PLUGIN_DIR,"cheat_sheets", sheetName)

    if exists(userSheet):
      sheet = userSheet
    elif exists(defaultSheet):
      sheet = defaultSheet
    dest_view = self.window.open_file(sheet)

    def set_view_props():
      if dest_view.is_loading():
        sublime.set_timeout(set_view_props, 50)
        return

    set_view_props()
    self.dest_view = dest_view

class CheatSheetTesterCommand(sublime_plugin.TextCommand):  
  def run(self, edit, **args):  
    sheetName = args["cheatsheet"] + ".cheatsheet"
    userSheet = join(sublime.packages_path(), "User/cheat_sheets", sheetName)
    defaultSheet = join(MY_PLUGIN_DIR,"cheat_sheets", sheetName)
    
    for value in userSheet, defaultSheet:
      if exists(value):
        print("File found:     %s" % value)
      else:
        print("File not found: %s" % value)


