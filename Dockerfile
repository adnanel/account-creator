FROM androidsdk/android-29

# RUN apt-get install -y cpu-checker qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
RUN echo "no" | avdmanager create avd  --name "Device" -k "system-images;android-29;google_apis;x86_64" --device "pixel_xl" --force

RUN mkdir /opt/work
WORKDIR /opt/work

ADD launch_avd.sh /opt/work/launch_avd.sh
RUN chmod +x /opt/work/launch_avd.sh

ENTRYPOINT ["bash", "-c", "/opt/work/launch_avd.sh"]

