# Variables
APP_NAME = Notepad==
BUILD_DIR = dist
INSTALL_DIR = /opt/matthewyang
BIN_LINK = /usr/local/bin/notepadee
DESKTOP_FILE = /usr/share/applications/notepadee.desktop

all: build

configure: ./configure

build:
	pyinstaller --hidden-import=tkinter -i Notepad.png src/$(APP_NAME).py
	cp Notepad.png dist/Notepad==/
	echo "Build completed. To install, run 'sudo make install'"

install:
	sudo mkdir -p $(INSTALL_DIR)
	sudo cp -R $(BUILD_DIR)/$(APP_NAME) $(INSTALL_DIR)/
	sudo ln -s $(INSTALL_DIR)/$(APP_NAME)/$(APP_NAME) $(BIN_LINK)
	sudo cp notepadee.desktop $(DESKTOP_FILE)
	sudo update-desktop-database
	echo "Install completed"

install-no-desktop-file:
	sudo mkdir -p $(INSTALL_DIR)
	sudo cp -R $(BUILD_DIR)/$(APP_NAME) $(INSTALL_DIR)/
	sudo ln -s $(INSTALL_DIR)/$(APP_NAME)/$(APP_NAME) $(BIN_LINK)
	echo "Install completed"

uninstall:
	sudo rm -rf /opt/matthewyang/$(APP_NAME)
	sudo rm -f $(BIN_LINK)
	sudo rm -rf $(DESKTOP_FILE)
	echo "Uninstalled. If issues experienced caused you to uninstall Notepad==, please report them on https://www.github.com/matthewyang204/NotepadEE."

uninstall-no-desktop-file:
	sudo rm -rf /opt/matthewyang/$(APP_NAME)
	sudo rm -f $(BIN_LINK)
	echo "Uninstalled. If issues experienced caused you to uninstall Notepad==, please report them on https://www.github.com/matthewyang204/NotepadEE."

clean:
	rm -rf dist
	rm -rf build
	rm -rf $(APP_NAME).spec
	echo "Cleaned all temp files used"

dist: clean
	mkdir ../temp
	cp -R ./* ../temp/
	tar -czf NotepadEE-Linux-src.tar.gz temp
	rm -rf ../temp

clean-dist: clean
	rm -rf NotepadEE-Linux-src.tar.gz
	rm -rf temp

upgrade: uninstall install

upgrade-no-desktop-file: uninstall-no-desktop-file install-no-desktop-file

.PHONY: configure build install clean
