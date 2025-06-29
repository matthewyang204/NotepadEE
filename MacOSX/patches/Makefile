ifeq ($(wildcard .configured),)
$(error You must run `./configure` before you can build.)
endif

ARCH ?= $(shell uname -m)
LDFLAGS := -L$(shell brew --prefix gettext)/lib -lintl
CPPFLAGS := -I$(shell brew --prefix gettext)/include

export LDFLAGS
export CPPFLAGS

.SILENT:

all: build

configure: ./configure

build:
# 	echo "Building..."
# 	# echo "Please select an architecture to build for:"
# 	# echo "1. 'x86_64' (Intel)"
# 	# echo "2. 'arm64' (Apple Silicon)"
# 	# # echo "3. 'universal' (Intel and Apple Silicon in a single fat binary, not currently supported)"
# 	# echo "Enter an architecture and press ENTER:"
# 	ARCH="$(ARCH)" && \
# 	echo "Building for architecture $$ARCH..." && \
# 	export ARCH && \
# 	nuitka --output-dir=dist --include-module=tkinter --enable-plugin=tk-inter --tcl-library-dir=$(shell brew --prefix tcl-tk)/lib --tk-library-dir=$(shell brew --prefix tcl-tk)/lib --macos-create-app-bundle --macos-target-arch="$$ARCH" --macos-app-icon=Notepad.png --macos-app-name="Notepad==" --macos-signed-app-name="com.matthewyang.NotepadEE" --macos-app-version=5.1.0 src/Notepad==.py
# 	# nuitka --debug --show-progress --show-scons --verbose --output-dir=dist --include-module=tkinter --enable-plugin=tk-inter --tcl-library-dir=$(shell brew --prefix tcl-tk)/lib --tk-library-dir=$(shell brew --prefix tcl-tk)/lib --macos-create-app-bundle --macos-target-arch="$$ARCH" --macos-app-icon=Notepad.png --macos-app-name="Notepad==" --macos-signed-app-name="com.matthewyang.NotepadEE" --macos-app-version=5.1.0 src/Notepad==.py
# 	echo "Build completed. Patching the app bundle..."
# 	cd dist/Notepad==.app/Contents && \
# 	mv MacOS/tk Resources/tk && \
# 	mv MacOS/tcl Resources/tcl && \
# 	cd MacOS && \
# 	ln -s ../Resources/tk ./tk && \
# 	ln -s ../Resources/tcl ./tcl && \
# 	ln -s ../Resources/tcl/tcl9.0 ./tcl9.0 && \
# 	ln -s ../Resources/tk/tk9.0 ./tk9.0
# 	echo "done"
	echo "Packaging..."

	echo "Creating directories..."
	mkdir -p dist/Notepad==.app/Contents
	mkdir -p dist/Notepad==.app/Contents/MacOS
	mkdir -p dist/Notepad==.app/Contents/Resources

	echo "Copying files..."
	cp assets/Info.plist dist/Notepad==.app/Contents/
	cp Notepad.png dist/Notepad==.app/Contents/Resources/
	cp src/Notepad==.py dist/Notepad==.app/Contents/MacOS/Notepad==.py

	echo "Patching files..."
	chmod +x dist/Notepad==.app/Contents/MacOS/Notepad==.py
	{ echo "#!/usr/bin/env python3\n\nimport os\nos.environ["DISPLAY"]\n:0.0\n"; cat dist/Notepad==.app/Contents/MacOS/Notepad==.py; } > /tmp/dcd072e14d6380b7f816d171d09d83ca394b554d5bac44a75c8336cac4f096c5 && mv /tmp/dcd072e14d6380b7f816d171d09d83ca394b554d5bac44a75c8336cac4f096c5 dist/Notepad==.app/Contents/MacOS/Notepad==.py

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

# sign:
# 	echo "Please enter the name of your certificate:"
# 	read CERTIFICATE && \
# 	echo "Signing..." && \
# 	sudo codesign --force --deep --sign "$$CERTIFICATE" dist/Notepad==.app
# 	echo "done"
