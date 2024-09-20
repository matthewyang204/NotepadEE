all: build

configure: ./configure

build:
	nuitka --macos-create-app-bundle \
		--macos-app-icon=Notepad.icns \
		--macos-app-version=custom-built \
		--macos-app-name="Notepad==" \
		--enable-plugin=tk-inter \
		--output-dir=dist Notepad==.py

	nuitka --macos-create-app-bundle \
		--macos-app-icon=Notepad.icns \
		--macos-app-version=custom-built \
		--macos-app-name="Notepad==" \
		--enable-plugin=tk-inter \
		--output-dir=dist/clone Clone/Notepad==.py
	mkdir dist/Notepad==.app/Contents/Resources/Clone
	mv dist/clone/Notepad==.app dist/Notepad==.app/Contents/Resources/Clone/
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
	echo "Cleaned all temp files used"

upgrade: uninstall-upgrade install

.PHONY: configure build install clean