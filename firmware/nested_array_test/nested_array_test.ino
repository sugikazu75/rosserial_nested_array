#include <ros.h>
#include <rosserial_nested_array/Points.h>

ros::NodeHandle nh;

rosserial_nested_array::Points pub_msg;
ros::Publisher pub("publisher", &pub_msg);

void subscriberCallback(const rosserial_nested_array::Points& msg){
  pub_msg = msg;
  pub.publish(&pub_msg);
}
ros::Subscriber<rosserial_nested_array::Points> sub("subscriber", &subscriberCallback);

void setup() {
  nh.initNode();
  nh.advertise(pub);
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(1);
}
