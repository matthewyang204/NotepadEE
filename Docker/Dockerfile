# Use Debian as the base image
FROM debian

# Install required packages
RUN apt-get update && yes | apt install git x11-apps sudo make

# Clone the repository and build the application
RUN git clone https://www.github.com/matthewyang204/NotepadEE.git /home/NotepadEE && cd /home/NotepadEE/Linux && yes | ./configure && make && sudo make install-no-desktop-file && cd /home && rm -rf NotepadEE

# Start the application
CMD ["notepadee"]