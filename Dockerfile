FROM duckietown/rpi-duckiebot-base:master18

COPY run_joy_cli.sh .

COPY joy_cli.py .

RUN [ "cross-build-start" ]

RUN chmod +x ./joy_cli.py

ENTRYPOINT ./run_joy_cli.sh

RUN [ "cross-build-end" ]
