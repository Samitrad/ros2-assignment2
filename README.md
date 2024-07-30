# ros2-assignment2
1. Overview

This project involves a ROS 2 setup with nodes for checking stock levels and delivering items. It includes:

    A StockCheckerServiceServer node that provides stock levels for items.
    A StockCheckerServiceClient node that queries stock levels and can request item deliveries.
    An ItemDeliveryActionServer node that processes delivery requests.
    An ItemDeliveryActionClient node that sends delivery requests and handles responses.

2. Project Structure
   Packages

    action_service: Contains the action server and client for item delivery.
    interface: Defines messages and actions used across the project.
3. Dependencies

    ROS 2 Humble: The project is built on ROS 2 Humble.
    Python 3.10: The project uses Python 3.10 for scripting.
    Matplotlib: Used for plotting stock levels.
 
4. Build the Project

    Source ROS 2 Setup:

source /opt/ros/humble/setup.bash

Build the Workspace:

colcon build

Source the Workspace Setup:

source install/setup.bash    

5. Launching the Nodes:

ros2 launch action_service action_service.launch.py



