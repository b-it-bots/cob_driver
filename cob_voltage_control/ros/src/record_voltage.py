#!/usr/bin/env python

import csv
import rospy
from cob_phidgets.msg import *
from std_msgs.msg import *

def callback(data):
	print "voltage=", data # voltage sensor is on the second port of the phidgets board
	writer.writerow( ( round((rospy.Time.now() - starttime).to_sec(),5), data) )

def record():
	rospy.init_node('record_voltage')
	global starttime
	starttime = rospy.Time.now()

	global f
	global writer
	filename = rospy.get_param("~filename")
	global port_voltage
	port_voltage = rospy.get_param("~port_voltage")

	f = open(filename, 'wt', 1)
	writer = csv.writer(f)
	writer.writerow(("time_from_start", "voltage"))

	rospy.Subscriber(port_voltage, Float64, callback)

	rospy.spin()

if __name__ == '__main__':
	record()

