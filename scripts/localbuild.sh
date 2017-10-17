#!/bin/bash

# This code should make it possible to clean out all caches of docker images that are specified in the docker-compose.yml
# and then rebuild all of them locally using docker-compose and then re-tag them with proper names.

# make nice exit
function niceexit {

    echo "$1"
    exit "$2"

}

# find all that needs to build tings with npm and build it before building docker
# (this might need change if path is not in root/<path>)
echo "# Doing npm installs"
for nodeservice in $(find . -iname "package.json" | grep -v node_modules | awk -F"/" '{print $2}'); do
    echo "# npm for $nodeservice"
    pushd "$nodeservice"
    docker run  -v /etc/passwd:/etc/passwd -v /etc/group:/etc/group -v "$PWD":/app -u $(id -u) --rm --workdir /app node /bin/bash -c "HOME=/tmp npm install && HOME=/tmp npm run build" || niceexit "Failed to build $nodeservice" 1
    popd
done

echo "# Build all images"
docker-compose build
niceexit "All done" 0
