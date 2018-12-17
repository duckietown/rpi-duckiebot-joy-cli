#!/usr/bin/env python
# license removed for brevity
import rospy
import sys

from sensor_msgs.msg import Joy

from __builtin__ import True


def keyCatcher(host):
    pub = rospy.Publisher('/'+host+'/joy', Joy, queue_size=1)
    rospy.init_node('joy-cli', anonymous=True)

    buttons = [0] * 11

    while not rospy.is_shutdown():
        input = raw_input('Enter direction(a,w,s,d) or lane-follow(start,stop)--> ')

        if input == 'w':
            axes = [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        elif input == 's':
            axes = [0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        elif input == 'd':
            axes = [0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0]
        elif input == 'a':
            axes = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
        elif input == 'start':
            # sends START to joystick (#7) to start lane-follow
            buttons[7] = 1
            axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        elif input == 'stop':
            # sends BACK to joystick (#6) to stop lane-follow
            buttons[6] = 1
            axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        else:
            axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        msg = Joy(header=None, axes=axes, buttons=buttons)
        pub.publish(msg)
        rospy.sleep(0.5)

        buttons = [0] * 11
        axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        msg = Joy(header=None, axes=axes, buttons=buttons)
        pub.publish(msg)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("No hostname specified!")
    else:
        hostname = sys.argv[1]

    try:
        keyCatcher(host = hostname)
    except rospy.ROSInterruptException:
        pass
