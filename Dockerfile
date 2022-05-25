FROM androidsdk/android-29

RUN apt update && apt install -y python python3 python3-pip python-setuptools nodejs npm
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --pre androidviewclient --upgrade
RUN pip3 install androidviewclient
RUN pip3 install requests

# RUN apt-get install -y cpu-checker qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
RUN echo "no" | avdmanager create avd  --name "Device" -k "system-images;android-29;google_apis;x86_64" --device "pixel_xl" --force

RUN mkdir /opt/work
WORKDIR /opt/work

ADD launch_avd.sh /opt/work/launch_avd.sh
RUN chmod +x /opt/work/launch_avd.sh

RUN mkdir /opt/work/app
ADD app /opt/work/app

RUN mkdir /opt/work/api
ADD sms-api /opt/work/api

RUN git clone https://github.com/dtmilano/AndroidViewClient.git /opt/work/app/avc

ENTRYPOINT ["bash", "-c", "/opt/work/launch_avd.sh"]

