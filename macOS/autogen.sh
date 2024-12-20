#!/bin/bash
@echo off

# First copy files from the Linux section of the repository
echo "Copying files..."
cp -R -v ../Linux/* ./
echo "done"

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
    
    # Build
    echo "Building..."
    make
    echo "done"
else
    echo "Configuration failed. Exiting."
    exit 1
fi
