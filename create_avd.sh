#!/bin/bash

# Configuration
androidSdkVersion="29"
deviceName="Device"
deviceProfile="pixel_xl" # See available profiles with: avdmanager list device
includePlayStore=false # See if SDK Version & Play Store are available together with: sdkmanager --list

# Obtain the AVD image
imageName="system-images;android-29;google_apis;x86_64"

# Create the AVD
echo /usr/lib/android-sdk/cmdline-tools/bin/avdmanager create avd \
  --abi google_apis/x86 \
  --device "$deviceProfile" \
  --force \
  --name "$deviceName" \
  --package "$imageName"
