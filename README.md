# Package `joy_cli` {#joy_cli}

<move-here src="#joy_cli"/>

## IMPORTANT

Use the `master18` branch, not this one.

## Testing

Run:

    $ python joy_cli.py $HOSTNAME

The robot should move when you press <kbd>a</kbd>, <kbd>w</kbd>, <kbd>s</kbd>, or <kbd>d</kbd>. You should press <kbd>Enter</kbd> afterwards and the robot will move for half a second in the desired direction.

## Dependencies

* `rospy`
* `sys`
* `sensor_msgs`
* `duckietown_msgs`
