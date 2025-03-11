.SILENT:

clean:
	cd Linux && make clean && cd ..
	cd macOS && ./autogen.sh clean && cd ..
	rm -rf build.txt

macos:
	cd macOS && ./configure && make -j$(nproc) && cd ..
	echo "macOS" > build.txt

linux:
	cd Linux && ./configure && make -j$(nproc) && cd ..
	echo "linux" > build.txt
