.SILENT:

all: build

configure: ./configure

build:
	echo "Building with Nuitka..."
	echo "Please select an architecture to build for:"
	echo "1. 'x86_64' (Intel)"
	echo "2. 'arm64' (Apple Silicon)"
	# echo "3. 'universal' (Intel and Apple Silicon in a single fat binary, not currently supported)"
	echo "Enter an architecture and press ENTER:"
	@read NUITKA_ARCH && \
	echo "Building for architecture $$NUITKA_ARCH..." && \
	export NUITKA_ARCH && \
	nuitka --output-dir=dist --include-module=tkinter --enable-plugin=tk-inter --macos-create-app-bundle --macos-target-arch="$$NUITKA_ARCH" --macos-app-icon=Notepad.png --macos-app-name="Notepad==" --macos-signed-app-name="com.matthewyang.NotepadEE" --macos-app-version=4.8.1 src/Notepad==.py
	echo "Nuitka build completed. To install, run 'sudo make install'. To upgrade, run 'sudo make upgrade'."

install:
	sudo mv "dist/Notepad==.app" /Applications/
	echo "Install successfull"

uninstall:
	sudo rm -rf /Applications/Notepad==.app
	sudo rm -rf ~/.notepadee
	echo "Uninstalled. If issues experienced caused you to uninstall Notepad==, please report them on https://www.github.com/matthewyang204/NotepadEE."

uninstall-upgrade:
	sudo rm -rf "/Applications/Notepad==.app"

clean:
	rm -rf dist
	rm -rf build
	rm -f Notepad==.spec
	echo "Cleaned all temp files used"

dist: clean
	mkdir ../temp
	cp -R ./* ../temp/
	tar -czvf NotepadEE-macOS-src.tar.gz -C ../temp .
	rm -rf ../temp

clean-dist: clean
	rm -rf NotepadEE-Linux-src.tar.gz
	rm -rf ../temp

upgrade: uninstall-upgrade install

sign:
	echo "Please enter the name of your certificate:"
	read CERTIFICATE && \
	echo "Signing..." && \
	sudo codesign --force --deep --sign "$$CERTIFICATE" dist/Notepad==.app
	echo "done"

.PHONY: configure build install uninstall uninstall-upgrade clean dist clean-dist upgrade
