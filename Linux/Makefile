# Variables
APP_NAME = Notepad==
BUILD_DIR = dist/$(APP_NAME)
INSTALL_DIR = /opt/matthewyang/$(APP_NAME)
BIN_LINK = /usr/local/bin/notepadee
DESKTOP_FILE = /usr/share/applications/notepadee.desktop

# Default target
all: configure build

# Target to configure the environment and build the application
configure:
	./configure

# Target to build the project
build: configure
	pyinstaller --windowed -i Notepad.png --hidden-import=tkinter $(APP_NAME).py

# Target to install the application
install: build
	sudo mkdir -p $(INSTALL_DIR)
	sudo cp dist/$(APP_NAME) $(INSTALL_DIR)/
	sudo ln -sf $(INSTALL_DIR)/$(APP_NAME) $(BIN_LINK)

	# Create a desktop file if --desktop flag is passed
	if [ "$(DESKTOP)" = "true" ]; then \
		echo "[Desktop Entry]" | sudo tee $(DESKTOP_FILE); \
		echo "Name=Notepad" | sudo tee -a $(DESKTOP_FILE); \
		echo "Exec=$(INSTALL_DIR)/$(APP_NAME)" | sudo tee -a $(DESKTOP_FILE); \
		echo "Icon=$(PWD)/Notepad.png" | sudo tee -a $(DESKTOP_FILE); \
		echo "Type=Application" | sudo tee -a $(DESKTOP_FILE); \
		echo "Terminal=false" | sudo tee -a $(DESKTOP_FILE); \
		sudo update-desktop-database; \
	fi

# Target to clean build artifacts
clean:
	rm -rf dist
	rm -rf build
	rm -rf $(APP_NAME).spec

.PHONY: all configure build install clean