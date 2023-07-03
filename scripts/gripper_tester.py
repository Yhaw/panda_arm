import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def publish_gripper_command():
    rospy.init_node('gripper_controller', anonymous=True)
    pub = rospy.Publisher('/arm_position_controller/panda_gripper_controller/command', JointTrajectory, queue_size=10)
    rate = rospy.Rate(1)  # 10 Hz (modify the rate as desired)

    while not rospy.is_shutdown():
        gripper_command = JointTrajectory()
        gripper_command.header.stamp = rospy.Time.now()
        gripper_command.joint_names = ['panda_finger_joint1']

        key = raw_input("Enter 'o' to open or 'g' to close: ")

        if key.lower() == 'o':
            open_position = JointTrajectoryPoint()
            open_position.positions = [0.04]  # Open position (modify as needed)
            open_position.time_from_start = rospy.Duration(0.1)  # Duration to hold the open position
            gripper_command.points.append(open_position)
        elif key.lower() == 'g':
            close_position = JointTrajectoryPoint()
            close_position.positions = [0.0]  # Close position (modify as needed)
            close_position.time_from_start = rospy.Duration(0.1)  # Duration to hold the close position
            gripper_command.points.append(close_position)

        if len(gripper_command.points) > 0:
            pub.publish(gripper_command)

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_gripper_command()
    except rospy.ROSInterruptException:
        pass
