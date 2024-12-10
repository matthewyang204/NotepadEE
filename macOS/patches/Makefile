all: build

configure: ./configure

build:
	pyinstaller --windowed --hidden-import=tkinter -i Notepad.png src/Notepad==.py
	sed -i '' 's/0\.0\.0/4\.6\.1/g' dist/Notepad==.app/Contents/Info.plist
	echo "Build completed. To install, run 'sudo make install'"
install:
	sudo mv dist/Notepad==.app /Applications/
	echo "Install successfull"

uninstall:
	sudo rm -rf /Applications/Notepad==.app
	sudo rm -rf ~/Library/Caches/NotepadEE
	sudo rm -rf ~/Library/Preferences/com.matthewyang.NotepadEE
	echo "Uninstalled. If issues experienced caused you to uninstall Notepad==, please report them on https://www.github.com/matthewyang204/NotepadEE."

uninstall-upgrade:
	sudo rm -rf /Applications/Notepad==.app

clean:
	rm -rf dist
	rm -rf build
	rm Notepad==.spec
	echo "Cleaned all temp files used"

upgrade: uninstall-upgrade install

.PHONY: configure build install clean
