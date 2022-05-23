#!/bin/bash

# Configuration
startEmulatorTimeout=18000 # Number of seconds to wait for emulator boot before quitting

avdmanager list avd

# Start the emulator
emulator -avd Device -no-boot-anim -no-window -no-audio -wipe-data &

# Wait for the boot to finish
# Thanks: https://gist.github.com/mrk-han/db70c7ce2dfdc8ac3e8ae4bec823ba51
animationState=""
failCounter=0

until [[ "$animationState" =~ "stopped" ]]; do
    animationState=$(adb -e shell getprop init.svc.bootanim 2>&1 &) # Checks state of emulator while in the boot animation

    if [[ "$animationState" =~ "device not found" || "$animationState" =~ "device offline" || "$animationState" =~ "running" ]]; then
        ((failCounter += 1))
        echo "Waiting for emulator to start... $failCounter"
        echo "Boot Animation State: $animationState"

        if [[ ${failCounter} -gt ${startEmulatorTimeout} ]]; then
            echo "Timeout of $startEmulatorTimeout seconds reached; failed to start emulator"
            exit 1
        fi
    fi

    sleep 1
done

sleep 10 # Give time for the launcher to appear
adb shell 'echo "chrome --disable-fre --no-default-browser-check --no-first-run" > /data/local/tmp/chrome-command-line'

echo "Emulator is ready!"

echo "Going into app dir..."
cd app
ls -ls

adb start-server

./script.sh

