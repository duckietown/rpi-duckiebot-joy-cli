#!/bin/bash

set -e -x

source /home/software/docker/env.sh

source /home/software/set_vehicle_name.sh $ROS_MASTER

python joy_cli.py $HOSTNAME

