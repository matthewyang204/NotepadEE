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
echo "done"
echo "Patching configure script..."
rm configure
cp patches/configure ./
echo "done"
echo "Patching Makefile..."
rm Makefile
cp patches/Makefile ./
echo "done"
echo "done"

# Configure the build
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
