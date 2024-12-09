#!/bin/bash
@echo off

# First copy files from the Linux section of the repository
echo "Copying files..."
cp -R -V ../Linux/* ./
echo "done"

# Patch the files
echo "Removing dpinstall..."
rm dpinstall
echo "done"
echo "Patching configure script..."
rm configure
cp patches/configure ./
echo "done"
