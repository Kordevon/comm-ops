FROM ros:humble

COPY int_publisher.py /int_publisher.py

RUN apt update && apt install -y python3-pip && pip3 install colcon-common-extensions

ENTRYPOINT ["bash", "-c", "source /opt/ros/humble/setup.bash && python3 /int_publisher.py $0 $1"]
