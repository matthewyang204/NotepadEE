#!/bin/bash
set +x

if [ "$1" == "clean" ]; then
    echo "Received 'clean' argument, removing everything copied over for building..."
    make clean
    rm -f Makefile
    rm -f Notepad.png
    rm -f configure
    rm -f notepadee.desktop
    rm -f requirements.txt
    rm -rf src
    echo "done"
    exit
fi

# First copy files from the Linux section of the repository
echo "Copying files..."
cp -R -v ../Linux/* ./
echo "done"

# Debugging exit to check if files have been properly copied
# Only enable if you need it
# exit 0

# Patch the files
echo "Patching files..."
echo "Removing dpinstall..."
rm dpinstall
echo "Patching configure script..."
rm configure
cp patches/configure ./
echo "Patching Makefile..."
rm Makefile
cp patches/Makefile ./
echo "Patching the key mappings..."
sed -i '' 's/<Control-/<Command-/g' src/Notepad==.py
echo "Patching the requirements..."
rm requirements.txt
cp patches/requirements.txt ./
echo "done"


# Debugging exit to check if files have been properly patched
# Only enable if you need it
# exit 0

# Make the configure script executable
echo "Making scripts executable"
chmod +x configure
echo "done"

# Configure the build
echo "Configuring build..."
./configure

# Check if the configure command was successful
if [ $? -eq 0 ]; then
    echo "Configuration successful. Proceeding to build..."
    make
    echo "done"
else
    echo "Configuration failed. Exiting."
    exit 1
fi
