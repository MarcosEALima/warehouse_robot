# Deprecated, kept for ROS 1 bridge.
# Use ApplyLinkWrench
# Apply Wrench to Gazebo Body.
# via the callback mechanism
# all Gazebo operations are made in world frame
string body_name                          # Gazebo body to apply wrench (linear force and torque)
                                          # wrench is applied in the gazebo world by default
                                          # body names are prefixed by model name, e.g. pr2::base_link
string reference_frame                    # wrench is defined in the reference frame of this entity
                                          # use inertial frame if left empty
                                          # frame names are bodies prefixed by model name, e.g. pr2::base_link
geometry_msgs/Point  reference_point      # wrench is defined at this location in the reference frame
geometry_msgs/Wrench wrench               # wrench applied to the origin of the body
builtin_interfaces/Time start_time        # (optional) wrench application start time (seconds)
                                          # if start_time is not specified, or
                                          # start_time < current time, start as soon as possible
builtin_interfaces/Duration duration      # optional duration of wrench application time (seconds)
                                          # if duration < 0, apply wrench continuously without end
                                          # if duration = 0, do nothing
                                          # if duration < step size, apply wrench
                                          # for one step size
