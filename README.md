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

## Todo

- Add automatic software detection using `#target`.
- Add AppleScript to open and run the script from the ExtendScript Toolkit.
- Add CoffeeScript support.

## Collaborators

Thanks to [@ZombieHippie](https://github.com/ZombieHippie) for [his shot](https://github.com/ZombieHippie/sublime-text-2-ExtendScript) at turning my [previous shell build system](https://github.com/seblavoie/After-Effects-Scripting-Sublime-Text-Package) into a real Sublime Text python plugin.
