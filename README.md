# QuickRulers - Sublime Text Plugin

This a **fork of [QuickRulers](https://github.com/FichteFoll/QuickRulers)**, a [Sublime Text 4](https://www.sublimetext.com/) plugin that provides easy access to the "rulers" setting.

Current '[**dev**](https://github.com/Gregory-K/QuickRulers)' branch is just a personal sandbox, nothing special.

For the time being, it provides:

- A setting for default set of rulers **@done**  
  Instead of always inserting your rulers preference at start,  
  QuickRulers panel will now open with the pre-populated user defaults.  
  _(something like "rulers display-toggle" and "define rulers" in one)_
- A python 3.8 only version for **Sublime Text 4** **@done**  
  It just runs on the ST4's python3.8 plugin host, nothing extra.


## Try

for whomsoever wants to try it  
_(take a look at ["Skip it"](#skip-it) if you just want to toggle rulers display)_

### Install

Remove "QuickRulers" from "Package Control", if previously installed.

Add to `Packages/User/Package Control.sublime-settings`,

```json
  "ignore_vcs_packages":
  [
    "QuickRulers"
  ]
```

#### Manual installation

1. Clone or download this repository (the default 'dev' branch for ST4 or the corresponding branch ST3 _see [Notes](#notes)_).
2. Rename the cloned or extracted root folder to `QuickRulers`.
3. Move the `QuickRulers` folder to your Sublime Text's `Packages` folder.  
   _To find the `Packages` folder, click menu `Preferences` > `Browse Packages`._
4. Restart Sublime Text, and go edit `Preferences > Package Settings > QuickRulers > Settings`.

_alt. way_  
1. Go to `Packages` folder.  
   _(if you don't know, click menu `Preferences` > `Browse Packages`)._
3. Create a directory named 'QuickRulers' and 'cd' inside it.
4. From command line
    - Default 'dev' branch (ST4)  
      `git clone --depth 1 https://github.com/Gregory-K/QuickRulers .`
    - 'dev-ST3' branch _see [Notes](#notes)_  
      `git clone --depth 1 --branch dev-ST3 https://github.com/Gregory-K/QuickRulers .`
4. Restart Sublime Text, and go edit `Preferences > Package Settings > QuickRulers > Settings`.

#### Update

Delete the contents of `Packages/Outline` folder and repeat the "Manual Installation",

OR

'cd' in `Packages/Outline` folder and  
`git fetch && git rebase` for Linux  
`git fetch; git rebase` for Windows

### Use

Create a key binding for the `quick_rulers` command, and use it.

Key-binding examples:

```json
[
  { "keys": ["alt+r"], "command": "quick_rulers" },
  { "keys": ["alt+shift+r"], "command": "quick_rulers",
    "args": {"show_current": false} }
]
```

![No words needed](http://i.imgur.com/lEKwdBc.gif)


## Notes

_Note: As mentioned above, this is a "playground". Expect rebases, resets, branch renaming._

Branches:  
'[**dev**](https://github.com/Gregory-K/QuickRulers)' : default branch for ST4.  
'[**dev-ST3**](https://github.com/Gregory-K/QuickRulers/tree/dev-ST3)' : branch for ST3.

Other Branches:  
'[**upstream**](https://github.com/Gregory-K/QuickRulers/tree/upstream)' : clone of the official upstream repository.  

**All credits** goes to the original author [**FichteFoll**](https://github.com/FichteFoll).


## Skip it

If you just want to toggle the display of rulers, you could do it with a key-binding set.

```json
{ "keys": ["alt+r"], "command": "set_setting",
  "args": {"setting": "rulers", "value": [79, 119]}
},
{ "keys": ["alt+shift+r"], "command": "set_setting",
  "args": {"setting": "rulers", "value": []}
},
```

_sorry, a simple one-key-binding to 'toggle_setting' works only with booleans and not with alternating values (ST4 limitation)_
