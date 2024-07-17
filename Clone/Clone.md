#Making new instances

The latest developer beta update to Notepad== allows you to create new instances in order to view/edit/save without autosave capabilities on macOS. You can directly compile the main .py file on the root of this repository, then compile the .py file in this directory. After compiling, move Notepad==.app inside of this directory into the main Notepad==.app's Contents/Resources/Clone/ directory.

If you decided to install the developer beta, you need to do this to verify the app instead of the normal way:
```
xattr -d com.apple.quarantine /Applications/Notepad==.app
xattr -d com.apple.quarantine /Applications/Notepad==.app/Contents/Resources/Clone/Notepad==.app
```
This will not only bypass the app itself, but the clone version inside of it.