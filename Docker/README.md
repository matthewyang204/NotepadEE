# Using Notepad== with Docker
You can find the instructions required to run the latest development build of the Linux version here on a Mac. This is only to test Linux builds. On Linux, you don't need to use docker to spin up a copy without wrecking your existing install. You only have to run `./configure && make && dist/Notepad==/Notepad==` to to do this.

Prerequisites:
- Clone this repository to wherever you like
- Navigate to this folder inside the cloned folder
- You have to have docker desktop installed. You can install it with homebrew via `brew install docker-desktop`.

Instructions:
1. You need to ensure you have XQuartz installed. If you have Homebrew, install it with `brew install xquartz`. If you already have it installed, skip this step.
2. Run `xhost + 127.0.0.1` to expose the XQuartz socket if you haven't already.
3. Build the docker image with `docker build -t notepadee .`.
4. You have to be inside this folder in order to start the docker image. To start, run this:
```
docker run -it \
  -e DISPLAY=host.docker.internal:0 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  notepadee
```