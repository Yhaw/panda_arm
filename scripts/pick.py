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
joint1_initial_position = 0
joint1_target_position = 1.09
joint1_duration = 13.5 # in seconds

joint2_topic = '/arm_position_controller/panda_joint2_position_controller/command'
joint2_initial_position = 0
joint2_target_position = 0.20
joint2_duration = 10  # in seconds

joint3_topic = '/arm_position_controller/panda_joint3_position_controller/command'
joint3_initial_position = 0
joint3_target_position = 0.61
joint3_duration = 10  # in seconds

joint4_topic = '/arm_position_controller/panda_joint4_position_controller/command'
joint4_initial_position = 0
joint4_target_position = -0.052
joint4_duration = 10  # in seconds

joint5_topic = '/arm_position_controller/panda_joint5_position_controller/command'
joint5_initial_position = 0
joint5_target_position = 0.54
joint5_duration = 10  # in seconds

joint6_topic = '/arm_position_controller/panda_joint6_position_controller/command'
joint6_initial_position = 0
joint6_target_position = 2.042
joint6_duration = 5  # in seconds

joint7_topic = '/arm_position_controller/panda_joint7_position_controller/command'
joint7_initial_position = 0
joint7_target_position = 0.409
joint7_duration = 5  # in seconds

# Initialize ROS node
rospy.init_node('joint_position_controller', anonymous=True)

# Create threads for joint movements
joint1_thread = Thread(target=move_joint, args=(joint1_topic, joint1_initial_position, joint1_target_position, joint1_duration))
joint2_thread = Thread(target=move_joint, args=(joint2_topic, joint2_initial_position, joint2_target_position, joint2_duration))
joint3_thread = Thread(target=move_joint, args=(joint3_topic, joint3_initial_position, joint3_target_position, joint3_duration))
joint4_thread = Thread(target=move_joint, args=(joint4_topic, joint4_initial_position, joint4_target_position, joint4_duration))
joint5_thread = Thread(target=move_joint, args=(joint5_topic, joint5_initial_position, joint5_target_position, joint5_duration))
joint6_thread = Thread(target=move_joint, args=(joint6_topic, joint6_initial_position, joint6_target_position, joint6_duration))
joint7_thread = Thread(target=move_joint, args=(joint7_topic, joint7_initial_position, joint7_target_position, joint7_duration))

# Start the threads
joint1_thread.start()
joint2_thread.start()
joint3_thread.start()
joint4_thread.start()
joint5_thread.start()
joint6_thread.start()
joint7_thread.start()

# Wait for the threads to finish
joint1_thread.join()
joint2_thread.join()
joint3_thread.join()
joint4_thread.join()
joint5_thread.join()
joint6_thread.join()
joint7_thread.join()


# import time
# import rospy
# from std_msgs.msg import Float64

# def move_joint(joint_topic, initial_position, target_position, duration):
#     start_time = time.time()
#     end_time = start_time + duration
    
#     pub = rospy.Publisher(joint_topic, Float64, queue_size=10)
#     rospy.init_node('joint_publisher', anonymous=True)
    
#     rate = rospy.Rate(100)  # Adjust the rate as per your requirements
    
#     while time.time() < end_time and not rospy.is_shutdown():
#         elapsed_time = time.time() - start_time
#         progress = elapsed_time / duration
#         current_position = initial_position + (target_position - initial_position) * progress
        
#         pub.publish(Float64(current_position))
#         rate.sleep()

#     rospy.loginfo("Joint {} reached target position: {}".format(joint_topic, target_position))

# # Example usage
# joint1_topic = '/arm_position_controller/panda_joint1_position_controller/command'
# joint1_initial_position = 0
# joint1_target_position = 1.57
# joint1_duration = 5  # in seconds

# joint2_topic = '/arm_position_controller/panda_joint2_position_controller/command'
# joint2_initial_position = 0
# joint2_target_position = -1.57
# joint2_duration = 7  # in seconds

# joint3_topic = '/arm_position_controller/panda_joint3_position_controller/command'
# joint3_initial_position = 0
# joint3_target_position = 0.785
# joint3_duration = 6  # in seconds

# joint4_topic = '/arm_position_controller/panda_joint4_position_controller/command'
# joint4_initial_position = 0
# joint4_target_position = -0.785
# joint4_duration = 4  # in seconds

# joint5_topic = '/arm_position_controller/panda_joint5_position_controller/command'
# joint5_initial_position = 0
# joint5_target_position = 1.0
# joint5_duration = 8  # in seconds

# joint6_topic = '/arm_position_controller/panda_joint6_position_controller/command'
# joint6_initial_position = 0
# joint6_target_position = -1.0
# joint6_duration = 5  # in seconds

# joint7_topic = '/arm_position_controller/panda_joint7_position_controller/command'
# joint7_initial_position = 0
# joint7_target_position = 0.5
# joint7_duration = 6  # in seconds

# # Initialize ROS node
# rospy.init_node('joint_position_controller', anonymous=True)

# # Create threads for joint movements
# joint1_thread = Thread(target=move_joint, args=(joint1_topic, joint1_initial_position, joint1_target_position, joint1_duration))
# joint2_thread = Thread(target=move_joint, args=(joint2_topic, joint2_initial_position, joint2_target_position, joint2_duration))
# joint3_thread = Thread(target=move_joint, args=(joint3_topic, joint3_initial_position, joint3_target_position, joint3_duration))
# joint4_thread = Thread(target=move_joint, args=(joint4_topic, joint4_initial_position, joint4_target_position, joint4_duration))
# joint5_thread = Thread(target=move_joint, args=(joint5_topic, joint5_initial_position, joint5_target_position, joint5_duration))
# joint6_thread = Thread(target=move_joint, args=(joint6_topic, joint6_initial_position, joint6_target_position, joint6_duration))
# joint7_thread = Thread(target=move_joint, args=(joint7_topic, joint7_initial_position, joint7_target_position, joint7_duration))

# # Start the threads
# joint1_thread.start()
# joint2_thread.start()
# joint3_thread.start()
# joint4_thread.start()
# joint5_thread.start()
# joint6_thread.start()
# joint7_thread.start()

# # Wait for the threads to finish
# joint1_thread.join()
# joint2_thread.join()
# joint3_thread.join()
# joint4_thread.join()
# joint5_thread.join()
# joint6_thread.join()
# joint7_thread.join()
