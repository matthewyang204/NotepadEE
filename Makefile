.SILENT:

clean:
	cd Linux && make clean && cd ..
	cd macOS && ./autogen.sh clean && cd ..

macos:
	cd macOS && ./configure && make -j$(nproc) && cd ..
	echo "export build = "macOS"" > build.txt
	chmod +x build.txt

linux:
	cd Linux && ./configure && make -j$(nproc) && cd ..
	echo "export build = "linux"" > build.txt
	chmod +x build.txt
