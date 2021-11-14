#!/bin/bash
# This builds and runs the script locally for testing purposes.
# Arguments: PLEX_USER PLEX_PASS PLEX_SERVER

docker build . -f Dockerfile --tag cmcucp:latest
docker run --rm cmcucp:latest $1 $2 $3 LocalTest
