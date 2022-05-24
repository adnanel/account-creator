#!/bin/bash

package=com.whatsapp
script=./whatsapp.py

echo "Installing apk..."
until adb install app.apk
do
  echo "Failed, trying again..."
done

echo "Installed! Running automation script..."

# Launch app
adb shell monkey -p $package 1

echo "Waiting for app to launch"
while [ -z "$(adb shell dumpsys window windows | grep $package)" ]
do
  echo "Still waiting for app to launch..."
done

echo "App is launched, starting script..."

python3 $script 387 "63 953 402" || echo "Failed!"

# Make screenshot
adb exec-out screencap -p > screen.png


sleep infinity
