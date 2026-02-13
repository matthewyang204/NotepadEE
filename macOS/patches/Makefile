ifeq ($(wildcard .configured),)
$(error You must run `./configure` before you can build.)
endif

ARCH ?= $(shell uname -m)
LDFLAGS := -L@gettext@/lib -lintl
CPPFLAGS := -I@gettext@/include

export LDFLAGS
export CPPFLAGS

.SILENT:

all: build

configure: ./configure

build:
	echo "Building..."
	# echo "Please select an architecture to build for:"
	# echo "1. 'x86_64' (Intel)"
	# echo "2. 'arm64' (Apple Silicon)"
	# # echo "3. 'universal' (Intel and Apple Silicon in a single fat binary, not currently supported)"
	# echo "Enter an architecture and press ENTER:"
	ARCH="$(ARCH)" && \
	echo "Building for architecture $$ARCH..." && \
	export ARCH && \
	nuitka --output-dir=dist --include-module=tkinter --include-data-dir="$(shell python3 -c "import spellchecker, os; print(os.path.join(os.path.dirname(spellchecker.__file__), 'resources'))")"="spellchecker/resources" --enable-plugin=tk-inter --tcl-library-dir=@tcl-tk8@/lib --tk-library-dir=@tcl-tk8@/lib --macos-create-app-bundle --macos-target-arch="$$ARCH" --macos-app-icon=Notepad.png --macos-app-name="Notepad==" --macos-signed-app-name="com.matthewyang.NotepadEE" --macos-app-version=5.3.0 src/Notepad==.py
	# nuitka --debug --show-progress --show-scons --verbose --output-dir=dist --include-module=tkinter --include-data-dir="$(shell python3 -c "import spellchecker, os; print(os.path.join(os.path.dirname(spellchecker.__file__), 'resources'))")"="spellchecker/resources" --enable-plugin=tk-inter --tcl-library-dir=@tcl-tk8@/lib --tk-library-dir=@tcl-tk8@/lib --macos-create-app-bundle --macos-target-arch="$$ARCH" --macos-app-icon=Notepad.png --macos-app-name="Notepad==" --macos-signed-app-name="com.matthewyang.NotepadEE" --macos-app-version=5.3.0 src/Notepad==.py
	echo "Build completed. Patching the app bundle..."
	cd dist/Notepad==.app/Contents && \
	mv MacOS/tk-files Resources/tk-files && \
	mv MacOS/tcl-files Resources/tcl-files && \
	cp ../../../Info.plist ./ && \
	cd MacOS && \
	ln -s ../Resources/tk-files ./tk-files && \
	ln -s ../Resources/tcl-files ./tcl-files && \
	ln -s ../Resources/tcl-files/tcl8.6 ./tcl8.6 && \
	ln -s ../Resources/tk-files/tk8.6 ./tk8.6
	cp -R scripts dist/Notepad==.app/Contents/Resources/
	chmod +x dist/Notepad==.app/Contents/Resources/scripts/*
	echo "done"
	echo "To install, run 'sudo make install'. To upgrade, run 'sudo make upgrade'."

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
	rm -f Notepad==.
	echo "Cleaned all temp files used"
	rm -rf nuitka-crash-report*.xml
	echo "Removed all old logs"

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
