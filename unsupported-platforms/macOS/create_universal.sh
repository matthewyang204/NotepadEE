#!/bin/bash

# Paths to the app bundles
APP_BUNDLE_X86_64="x86_64.app"
APP_BUNDLE_ARM64="arm64.app"
OUTPUT_BUNDLE="Notepad==.app"

# Ensure the output directory does not exist, or remove it if it does
if [ -d "$OUTPUT_BUNDLE" ]; then
    rm -rf "$OUTPUT_BUNDLE"
fi

# Copy the x86_64 app bundle to the output location
cp -R "$APP_BUNDLE_X86_64" "$OUTPUT_BUNDLE"

# Function to merge binaries
merge_binaries() {
    local x86_64_file=$1
    local arm64_file=$2
    local output_file=$3

    if [ -f "$arm64_file" ]; then
        lipo -create -output "$output_file" "$x86_64_file" "$arm64_file"
    else
        echo "Warning: $arm64_file does not exist."
    fi
}

# Find all executable files and dylibs in the app bundle
find "$OUTPUT_BUNDLE" -type f \( -perm +111 -o -name '*.dylib' \) | while read -r file; do
    relative_path="${file#$OUTPUT_BUNDLE/}"
    x86_64_file="$APP_BUNDLE_X86_64/$relative_path"
    arm64_file="$APP_BUNDLE_ARM64/$relative_path"
    output_file="$file"

    merge_binaries "$x86_64_file" "$arm64_file" "$output_file"
done

echo "Merging complete. Universal app bundle created at: $OUTPUT_BUNDLE"
