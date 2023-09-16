#!/usr/bin/python3
from launch import LaunchDescription, LaunchContext
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, DeclareLaunchArgument, OpaqueFunction, LogInfo, RegisterEventHandler, EmitEvent, IncludeLaunchDescription
from launch.event_handlers import OnProcessStart, OnExecutionComplete, OnProcessExit
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
import yaml
import os

def generate_launch_description():
    my_pkg = get_package_share_directory('draw_fibo')

    spawn_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(my_pkg,'launch','spawn_4turtles.launch.py')
        ),
        launch_arguments=None
    )
    PCS_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(my_pkg,'launch','PCS.launch.py')
        ),
        launch_arguments=None
    )
    launch_description = LaunchDescription()
    launch_description.add_action(spawn_launch)
    launch_description.add_action(PCS_launch)
    return launch_description