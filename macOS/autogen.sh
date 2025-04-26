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
    rm -f requirements-3.4.txt
    rm -rf src
    rm -rf resources
    echo "done"
    exit
fi

if [ "$1" == "rebuild" ]; then
    echo "Received 'rebuild' argument, removing everything copied over for building and then doing a fresh build..."
    make clean
    rm -f Makefile
    rm -f Notepad.png
    rm -f configure
    rm -f notepadee.desktop
    rm -f requirements.txt
    rm -f requirements-3.4.txt
    rm -rf src
    rm -rf resources
    echo "done"
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
echo "Removing resources"
rm -rf resources
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
rm requirements-3.4.txt
cp patches/requirements-3.4.txt ./
echo "Patching the README..."
rm README.md
cp patches/README.md ./
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
    HOST_ARCH=$(uname -m)
    if [ "$1" == "--arch=x86_64" ]; then
        echo "Building with selected architecture x86_64..."
        make ARCH=x86_64
    elif [ "$1" == "--arch=arm64" ]; then
        echo "Building with selected architecture arm64..."
        make ARCH=arm64
    elif [ "$1" == "--arch=universal" ]; then
        echo "Building with selected architecture universal..."
        make ARCH=universal
    else
        echo "Building with default host architecture, $HOSTARCH..."
        make
    fi
    echo "done"
else
    echo "Configuration failed. Exiting."
    exit 1
fi
