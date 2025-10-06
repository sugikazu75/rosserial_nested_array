#!/usr/bin/env python

import rospy
import time
from rosserial_nested_array.msg import Point, Points

rospy.init_node("rosserial_test_node")

pub = rospy.Publisher("subscriber", Points, queue_size=10)

time.sleep(1)

pub_msg = Points()

point1 = Point()
point1.point.append(1)
point1.point.append(2)
point1.point.append(3)
pub_msg.points.append(point1)

point2 = Point()
point2.point.append(4)
point2.point.append(5)
pub_msg.points.append(point2)

point3 = Point()
point3.point.append(6)
point3.point.append(7)
point3.point.append(8)
point3.point.append(9)
pub_msg.points.append(point3)

pub.publish(pub_msg)

time.sleep(2)


pub_msg = Points()

point1 = Point()
point1.point.append(10)
point1.point.append(20)
point1.point.append(30)
pub_msg.points.append(point1)
point2 = Point()
point2.point.append(40)
point2.point.append(50)
pub_msg.points.append(point2)
point3 = Point()
point3.point.append(60)
point3.point.append(70)
point3.point.append(80)
point3.point.append(90)
pub_msg.points.append(point3)
pub.publish(pub_msg)
