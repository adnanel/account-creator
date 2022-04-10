FROM ubuntu:20.04

RUN dpkg --add-architecture i386 && apt-get update && apt-get -y install libc6:i386 libncurses5:i386 libstdc++6:i386
RUN apt-get -y install android-sdk-platform-tools android-sdk android-sdk-build-tools-common android-sdk-build-tools
RUN apt-get -y install android-platform-tools-base android-sdk-helper
RUN apt-get -y install openjdk-8-jdk
RUN apt-get -y install wget unzip

# Setup android SDK
RUN echo "export ANDROID_HOME=/usr/lib/android-sdk">>/root/.bashrc
RUN export ANDROID_HOME=/usr/lib/android-sdk

RUN mkdir /opt/sdk
WORKDIR /opt/sdk
RUN wget -O cmdtools.zip https://dl.google.com/android/repository/commandlinetools-linux-8092744_latest.zip
RUN unzip cmdtools.zip -d /usr/lib/android-sdk

RUN /usr/lib/android-sdk/cmdline-tools/bin/sdkmanager --sdk_root=$ANDROID_HOME --install 'extras;google;m2repository' 'extras;android;m2repository' 'cmdline-tools;latest' 'build-tools;29.0.2' 'platform-tools' 'platforms;android-29' 'tools' 'cmdline-tools;latest' 'emulator' 'system-images;android-29;default;x86_64' 'system-images;android-29;google_apis;x86_64'
RUN /usr/lib/android-sdk/cmdline-tools/bin/sdkmanager --sdk_root=$ANDROID_HOME --install 'system-images;android-29;default;x86' 'system-images;android-29;google_apis;x86'
RUN yes | /usr/lib/android-sdk/cmdline-tools/bin/sdkmanager --sdk_root=$ANDROID_HOME --update
RUN yes | /usr/lib/android-sdk/cmdline-tools/bin/sdkmanager --sdk_root=$ANDROID_HOME --licenses

RUN mkdir /opt/work
WORKDIR /opt/work

# download selenoid
RUN wget -O selendroid.jar https://github.com/selendroid/selendroid/releases/download/0.17.0/selendroid-standalone-0.17.0-with-dependencies.jar
RUN wget -O selendroid-test.apk https://search.maven.org/remotecontent?filepath=io/selendroid/selendroid-test-app/0.17.0/selendroid-test-app-0.17.0.apk

ADD runner.sh /opt/work
ADD create_avd.sh /opt/work
ADD launch_avd.sh /opt/work

RUN /opt/work/create_avd.sh
RUN /opt/work/launch_avd.sh


ENTRYPOINT ["bash"]

