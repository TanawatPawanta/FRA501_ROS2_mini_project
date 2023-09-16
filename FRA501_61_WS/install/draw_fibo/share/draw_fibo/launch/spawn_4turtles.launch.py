#!/usr/bin/python3
from launch import LaunchDescription, LaunchContext
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, DeclareLaunchArgument, OpaqueFunction, LogInfo, RegisterEventHandler, EmitEvent
from launch.event_handlers import OnProcessStart, OnExecutionComplete, OnProcessExit
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import yaml
import os


def generate_launch_description():
    x_launch_arg = DeclareLaunchArgument('x', default_value='1.0',description="spawn x:float")
    x = LaunchConfiguration('x')

    y_launch_arg = DeclareLaunchArgument('y', default_value='1.0',description="spawn y:float")
    y = LaunchConfiguration('y')
    tao_name = ['Foxy', 'Noetic', 'Humble', 'Iron']
    # tao_name = ['Humble']
    turtlesimplus_node = Node(
        package='turtlesim_plus',
        executable='turtlesim_plus_node.py'
    )

    # kill
    kill_cmd = LaunchConfiguration(
        'cmd',default=['ros2 service call /remove_turtle turtlesim/srv/Kill "{name: \'turtle1\'}"']
    )
    kill_turtle = ExecuteProcess(
        cmd = [[kill_cmd]],
                shell = True
    )
    kill_event = RegisterEventHandler(
        OnProcessStart(
            target_action=turtlesimplus_node,
            on_start=[
                LogInfo(msg='Killing turtle...'),
                kill_turtle
            ]
        )
    )

    launch_description = LaunchDescription()
    launch_description.add_action(x_launch_arg)
    launch_description.add_action(y_launch_arg)
    launch_description.add_action(turtlesimplus_node)
    launch_description.add_action(kill_event)
    for i in tao_name:
        name = i
        # spawn
        spawn_cmd = LaunchConfiguration(
            'cmd',default = ['ros2 service call /spawn_turtle turtlesim/srv/Spawn "{x: ',x,', y: ',y,', theta: 0.0, name: \'',name,'\'}"']
            )
        spawn_turtle = ExecuteProcess(
            cmd = [[spawn_cmd]],
            shell = True
            )
        # spawn_event = RegisterEventHandler(
        #     OnExecutionComplete(
        #         target_action=kill_turtle,
        #         on_completion=[
        #             LogInfo(msg='Spawning turtle...'),
        #             spawn_turtle
        #         ]
        #     )
        # )
        launch_description.add_action(spawn_turtle)

    return launch_description

