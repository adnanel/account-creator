#!/bin/bash

adb start-server

# Launch whatsapp
adb shell monkey -p com.whatsapp 1

python3 ./whatsapp.py

# Make screenshot
adb exec-out screencap -p > screen.png


sleep infinity
