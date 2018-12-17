# Package `joy_cli` {#joy_cli}

<move-here src="#joy_cli"/>


## Testing

Run:

    $ python joy_cli.py $HOSTNAME

The robot should move when you press <kbd>a</kbd>, <kbd>w</kbd>, <kbd>s</kbd>, or <kbd>d</kbd>. You should press <kbd>Enter</kbd> afterwards and the robot will move for half a second in the desired direction.

To initiate (or stop) the lane-following demo, enter `start` (or `stop`) and press <kbd>Enter</kbd>.

You can also run it as a Docker container:

    docker -H HOSTNAME.local run -it --rm --privileged --network=host -v /data:/data duckietown/rpi-duckiebot-joy-cli:master18

Or if you have Duckietown shell simply as:

    $ dts duckiebot keyboard_control hostname --cli

## Dependencies

* `rospy`
* `sys`
* `sensor_msgs`
* `duckietown_msgs`
