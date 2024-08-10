# Variables
APP_NAME = Notepad==
BUILD_DIR = dist/$(APP_NAME)
INSTALL_DIR = /opt/matthewyang
BIN_LINK = /usr/local/bin/notepadee
DESKTOP_FILE = /usr/share/applications/notepadee.desktop

all: build

configure: ./configure

build:
	pyinstaller --windowed -i Notepad.png --hidden-import=tkinter $(APP_NAME).py
	echo "Build completed. To install, run 'sudo make install'"

install:
	sudo mkdir -p $(INSTALL_DIR)
	sudo cp -R dist/$(APP_NAME) $(INSTALL_DIR)/$(APP_NAME)
	sudo ln -s $(INSTALL_DIR)/$(APP_NAME)/$(APP_NAME) $(BIN_LINK)
	echo "[Desktop Entry]" | sudo tee $(DESKTOP_FILE); \
	echo "Name=Notepad" | sudo tee -a $(DESKTOP_FILE); \
	echo "Exec=$(BIN_LINK)" | sudo tee -a $(DESKTOP_FILE); \
	echo "Icon=$(INSTALL_DIR)/$(APP_NAME)/Notepad.png" | sudo tee -a $(DESKTOP_FILE); \
	echo "Type=Application" | sudo tee -a $(DESKTOP_FILE); \
	echo "Terminal=false" | sudo tee -a $(DESKTOP_FILE); \
	sudo update-desktop-database

	echo "Install completed"

uninstall:
	sudo rm -rf /opt/matthewyang/$(APP_NAME)
	sudo rm -f $(BIN_LINK)
	echo "Uninstalled. If issues experienced caused you to uninstall Notepad==, please report them on https://www.github.com/matthewyang204/NotepadEE."

clean:
	rm -rf dist
	rm -rf build
	rm -rf $(APP_NAME).spec
	echo "Cleaned all temp files used"

upgrade:uninstall install

.PHONY: configure build install clean