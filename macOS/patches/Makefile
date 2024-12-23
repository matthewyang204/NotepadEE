.SILENT:

all: build

configure: ./configure

build:
	echo "Building with PyInstaller..."
	pyinstaller --windowed --hidden-import=tkinter -i Notepad.png src/Notepad==.py
	sed -i '' 's/0\.0\.0/4\.7\.4/g' dist/Notepad==.app/Contents/Info.plist
	echo "Build completed. To install, run 'sudo make install'. To upgrade, run 'sudo make upgrade'."

build-nuitka:
	echo "Installing required libraries for Nuitka to fix icon..."
	pip3 install imageio --break-system-packages
	echo "Building with Nuitka..."
	echo "Please select an architecture to build for:"
	echo "1. 'x86_64' (Intel)"
	echo "2. 'arm64' (Apple Silicon)"
	# echo "3. 'universal' (Intel and Apple Silicon in a single fat binary, not currently supported)"
	echo "Enter an architecture and press ENTER:"
	read NUITKA_ARCH
	nuitka --include-module=tkinter --output-dir=dist --macos-create-app-bundle --macos-target-arch=$(NUITKA_ARCH) --macos-app-icon=Notepad.png --macos-app-name="Notepad==" --macos-signed-app-name="com.matthewyang.NotepadEE" --macos-app-version=4.7.4 src/Notepad==.py
	echo "Nuitka build completed. To install, run 'sudo make install'. To upgrade, run 'sudo make upgrade'."

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

clean-nuitka:
	rm -rf dist
	rm -rf build
	echo "Cleaned all temp files used in Nuitka build"

dist: clean
	mkdir ../temp
	cp -R ./* ../temp/
	tar -czvf NotepadEE-macOS-src.tar.gz -C ../temp .
	rm -rf ../temp

clean-dist: clean
	rm -rf NotepadEE-Linux-src.tar.gz
	rm -rf ../temp

upgrade: uninstall-upgrade install

.PHONY: configure build install uninstall uninstall-upgrade clean dist clean-dist upgrade
