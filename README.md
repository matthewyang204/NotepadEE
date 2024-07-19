# Notepad==
Simple notepad for Macs

System requirements:

Apple Silicon Version: macOS 11.0 or above

Intel Silicon Version: macOSX 10.4 or above

You can download prebuilt binaries in the Releases

Binaries are now signed

After downloading the binary, extracting the .zip file, and moving the unzipped app to the Applications folder on your root drive, run this to bypass gatekeeper if it doesn't show a blue open button in the popup:
```
xattr -d com.apple.quarantine /Applications/Notepad==.app
xattr -d com.apple.quarantine /Applications/Notepad==.app/Contents/Resources/Clone/Notepad==.app
```

Note: The feature of launching a new instance does not work unless the app bundle is placed in /Applications in the root of your Mac's drive.

Linux:
- Older x.1.x releases will work on Linux when compiled from source
- Latest x.1.x version is 3.1.x
- Download latest dev source code from the Linux repository: https://github.com/matthewyang204/NotepadEE-x.1.x
- Download latest release source code for Linux, 3.1.2, here: https://github.com/matthewyang204/NotepadEE/releases/tag/3.1.2
