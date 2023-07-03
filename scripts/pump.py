import time
import rospy
from std_msgs.msg import Float64
from threading import Thread

def move_joint(joint_topic, initial_position, target_position, duration):
    start_time = time.time()
    end_time = start_time + duration
    
    pub = rospy.Publisher(joint_topic, Float64, queue_size=10)
    
    rate = rospy.Rate(100)  # Adjust the rate as per your requirements
    
    # Publish the initial position
     
    # Wait for 10 seconds
     
    while time.time() < end_time and not rospy.is_shutdown():
        elapsed_time = time.time() - start_time
        progress = elapsed_time / duration
        current_position = initial_position + (target_position - initial_position) * progress
        
        pub.publish(Float64(current_position))
        rate.sleep()

    rospy.loginfo("Joint {} reached target position: {}".format(joint_topic, target_position))

# Example usage
joint1_topic = '/arm_position_controller/panda_joint1_position_controller/command'
joint1_initial_position = 1.09
joint1_target_position = -1.89
joint1_duration = 15  # in seconds

joint2_topic = '/arm_position_controller/panda_joint2_position_controller/command'
joint2_initial_position = 0.20
joint2_target_position = 0.121
joint2_duration = 13  # in seconds

joint5_topic = '/arm_position_controller/panda_joint5_position_controller/command'
joint5_initial_position = 0.54
joint5_target_position = 0.43
joint5_duration = 5  # in seconds


joint6_topic = '/arm_position_controller/panda_joint6_position_controller/command'
joint6_initial_position = 2.042
joint6_target_position = 2.27
joint6_duration = 8  # in seconds



# Initialize ROS node
rospy.init_node('joint_position_controller', anonymous=True)

# Create threads for joint movements
joint1_thread = Thread(target=move_joint, args=(joint1_topic, joint1_initial_position, joint1_target_position, joint1_duration))
joint2_thread = Thread(target=move_joint, args=(joint2_topic, joint2_initial_position, joint2_target_position, joint2_duration))
joint5_thread = Thread(target=move_joint, args=(joint5_topic, joint5_initial_position, joint5_target_position, joint5_duration))
joint6_thread = Thread(target=move_joint, args=(joint6_topic, joint6_initial_position, joint6_target_position, joint6_duration))
 
# Start the threads
joint1_thread.start()
joint2_thread.start()
joint5_thread.start()
joint6_thread.start()
 
# Wait for the threads to finish
joint1_thread.join()
joint2_thread.join()
joint5_thread.join()
joint6_thread.join()
 