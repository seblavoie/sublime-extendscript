# ExtendScript for Sublime Text

A plugin to help with ExtendScript development workflow. It's really basic but it might be helpful. Feel free to contribute!

## What it does?

### Copies the current script to the desired software's script folder

Use `⌘+⇧+P` and chose between the options.

- ExtendScript: Build for After Effects
- ExtendScript: Build for Photoshop
- ExtendScript: Build for Illustrator
- ExtendScript: Build for InDesign

### `#include` compilation

`#include` statements are useful when developping but not as much when you want to ship a single .jsx file. This will replace `#include` line with the actual code.

Look at ExtendScript.sublime-settings if you want to turn this off.

### Automatically sets `debug` to false

You'll probably want to have a debug variable or property somewhere to help you test your code with the ExtendScript Toolkit. You may also want it turned off when testing it from within your application UI.

## Installation

### Sublime Package Control

The preferred method of installation is via [Sublime Package Control](http://wbond.net/sublime_packages/package_control).

1. [Install Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation)
2. From inside Sublime Text 2, open Package Control's Command Pallet: `Ctrl`+`Shift`+`P` (Windows, Linux) or `⌘`+`⇧`+`P` on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `ExtendScript` and hit Return. The package will be downloaded to the appropriate directory.
5. Restart Sublime Text 2 to complete installation.

### Manual Installation

1. Download or clone this repository to a directory `ExtendScript` in the Sublime Text 2 Packages directory for your platform:
    * Mac: `git clone https://github.com/seblavoie/sublime-extendscript.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/ExtendScript`
    * Windows: `git clone https://github.com/seblavoie/sublime-extendscript.git %APPDATA%\Sublime/ Text/ 2/\ExtendScript`
    * Linux: `git clone https://github.com/seblavoie/sublime-extendscript.git ~/.Sublime\ Text\ 2/Packages/ExtendScript`
2. Restart Sublime Text 2 to complete installation.

## Todo

- Add automatic software detection using `#target`.
- Add AppleScript to open and run the script from the ExtendScript Toolkit.
- Add CoffeeScript support.

## Collaborators

Thanks to [@ZombieHippie](https://github.com/ZombieHippie) for [his shot](https://github.com/ZombieHippie/sublime-text-2-ExtendScript) at turning my [previous shell build system](https://github.com/seblavoie/After-Effects-Scripting-Sublime-Text-Package) into a real Sublime Text python plugin.
