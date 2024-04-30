#!/bin/sh

echo "Installing dependencies..."

echo "Checking for Homebrew..."
# Check for Homebrew
if test ! $(which brew); then
    echo "no. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "yes."
fi

echo "Checking for node..."
# Check for Node.js and npm
if test ! $(which node); then
    echo "no. Installing..."
    brew install node
else
    echo "yes"
fi

echo "Checking for node..."
if test ! $(which npm); then
    echo "no. Installing..."
    brew install npm
else
    echo "yes."
fi

echo "Checking for npx..."
# Check for npx
if test ! $(which npx); then
    echo "no. Installing..."
    npm install -g npx
else
    echo "yes"
fi
