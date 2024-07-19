# Making new instances

The latest update to Notepad== allows you to create new instances in order to view/edit/save multiple files without autosave capabilities at the same time on macOS. This feature does not work unless the .app bundle is placed in /Applications in the root of your Mac's drive.

To verify the app:
```
xattr -d com.apple.quarantine /Applications/Notepad==.app
xattr -d com.apple.quarantine /Applications/Notepad==.app/Contents/Resources/Clone/Notepad==.app
```
This will not only bypass the app itself, but the clone version inside of it.