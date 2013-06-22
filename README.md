# Cheater Sublime Text 2 Plugin

Cheater is a plugin for quickly accessing cheat sheets in the Sublime Text 2 editor. Typing the key sequence will open a cheat sheet in a new file tab. If the sheet is already open, it will simply pop to the front.

## Available Cheat Sheets

At the moment there is only one available sheet.

* Regular Expressions "cmd/ctrl + shift + c" + "r" + "x"

## How to add your own Cheat Sheets

* In your `./Packages/User/` folder create a folder named `cheat_sheet` and add your filename.cheatsheet. Highlighting follows the following format:

```
Header
\t Text
Command \s\s Text
```

* Add a keyboard shortcut by adding the following line to `./Packages/User/Default(OS).sublime-keymap` and change the keys and filename:

```
{ "keys": ["ctrl+shift+c", "n", "s"], "command": "cheat_sheet", "args": {"cheatsheet": "filename"} }
```

* Add a menu entry by adding the following to `./Packages/User/Main.sublime-menu and change both instances of filename:

```
[
  {
    "id": "tools",
    "children": [
      {
        "id": "cheat-sheets",
        "caption": "Cheat Sheets",
        "children": [
          {
            "caption": "filename",
            "command": "cheat_sheet",
            "args": {"cheatsheet": "filename"}
          }
        ]
      }
    ]
  }
]
```

## Note on Patches/Pull Requests

New sheets, and improvements to the existing ones are more than welcome.

* Fork the project.
* Make your feature addition or bug fix.
* Add tests for it. This is important so I don't break it in a future version unintentionally.
* Commit, but do not mess with the Rakefile. If you want to have your own version, that is fine but bump the version in a commit by itself in another branch so I can ignore it when I pull.
* Send me a pull request. Bonus points for git flow feature branches.

## License

Cheater is licensed under the MIT License. See LICENSE for details.
