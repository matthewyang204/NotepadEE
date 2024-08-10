#!/bin/sh

# Check if we're on macOS or Linux and set DISPLAY accordingly
if [ "$(uname)" = "Darwin" ]; then
    # macOS
    export DISPLAY=host.docker.internal:0
else
    # Linux
    export DISPLAY=:0
fi

# Execute the command passed to the container
exec "$@"