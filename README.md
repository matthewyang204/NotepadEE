# Notepad==
Simple notepad for computers without simple-enough notepad software

Mac system requirements:

Apple Silicon Version: macOS 11.0 or above

Intel Silicon Version: macOSX 10.4 or above

Just about any GUI Linux version released in the last 20-25 years should work

You can download prebuilt Mac and Linux binaries in the Releases.

Linux binaries are only AMD64

install-linux.sh can be downloaded to your Downloads folder and run 
```
sh ~/Downloads/install-linux.sh
```
Enter your password if prompted because some parts of the script requires administrator (sudo) priveleges

Separate setup-mac-[your cpu architecture].command CLI installation wizard can be downloaded to Downloads folder before double-clicking to launch. If it prompts you that the app is not from an identified developer, you can open up a terminal window, type in 
```
xattr -d com.apple.quarantine 
```
and drag the .command installer into the terminal window. Press Enter and your thing will no longer prompt you about the unidentified developer thing.

If the installer window doesn't open still, then type 
```
chmod +x
```
and then drag the .command file into the window. And then try again.

Enter your password if prompted because some parts of the script requires administrator (sudo) priveleges
