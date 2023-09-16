#!/usr/bin/python3
from launch import LaunchDescription, LaunchContext
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, DeclareLaunchArgument, OpaqueFunction, LogInfo, RegisterEventHandler, EmitEvent
from launch.event_handlers import OnProcessStart, OnExecutionComplete, OnProcessExit
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import yaml
import os
def modify_config_namespace(path:str, new_path:str, namespace:str)->None:
    with open(path,'r') as file:
        data = yaml.load(file, Loader=yaml.SafeLoader)

    new_data = {namespace: data}

    with open(new_path,'w') as file:
        yaml.dump(new_data,file)

def generate_launch_description():
    tao_name = ['Foxy', 'Noetic', 'Humble', 'Iron']
    # tao_name = ['Humble']
    launch_description = LaunchDescription()
    my_pkg = get_package_share_directory('draw_fibo')
    config_param_path = os.path.join(my_pkg,'config','parameters.yaml')
    config_vp_path = os.path.join(my_pkg,'via_point','via_point_test.yaml')
    for i in tao_name:
        ns = i
        new_config_param_path = os.path.join(my_pkg,'config','parameters_'+ns+'.yaml')
        new_config_vp_path = os.path.join(my_pkg,'via_point','via_point_'+ns+'.yaml')
        modify_config_namespace(config_param_path, new_config_param_path, ns)
        tao_planning_node = Node(
            package='turtlesim_plus_planning',
            executable='tao_planning.py',
            parameters=[
                {'namespace':i},
                {'new_file_path':new_config_vp_path}
            ]
        )
        tao_controller_node = Node(
            package='turtlesim_plus_controller',
            executable='tao_controller.py',
            namespace=i,
            parameters=[new_config_param_path]
        )
        tao_scheduler_node = Node(
            package='turtlesim_plus_scheduler',
            executable='tao_scheduler.py',
            namespace=i,
            arguments=['-f',new_config_vp_path]
        )
        launch_description.add_action(tao_planning_node)
        launch_description.add_action(tao_controller_node)
        launch_description.add_action(tao_scheduler_node)
    
    return launch_description

# path = '/home/tanawatp/FRA501_61_WS/src/draw_fibo/via_point/via_point_00.yaml'
# with open(path,'r') as file:
#     data = yaml.load(file, Loader=yaml.SafeLoader)
# vp = data['via_points']
# print("vp[0] : ",vp[0])
# p = vp[0]
# print(len(vp))
# print("vp[0] type : ",type(vp[0]))
# print("data :", vp)
# wp = []

# for i in range(20):
#     if(i<10):
#         temp = [1.5,6+0.3*i]
#         wp.append(temp)
#     elif(i>=10 and i<15):
#         temp = [1.5+0.2*(i-9),9.0]
#         wp.append(temp)        
#     else:
#         temp = [1.5+0.2*(i-15),8.0]
#         wp.append(temp)
# print(len(wp))
# print("wp : ",wp)

# wp=[]
# for i in range(20):
#     if(i<8):
#         temp = [1.5,3.5+0.2*i]
#     elif(i>=8 and i<11):
#         temp = [1.5+0.2*(i-7),5.1-0.2*(i-7)]
#     elif(i>=12 and i<14):
#         temp = [1.5+0.2*(i-10),4.3+0.2*(i-10)]
#     elif(i>=14 and i<16):
#         temp = [1.5+0.2*(i-13),4.3-0.2*(i-13)]
#     else:
#         temp = [1.5+0.2*(i-16),3.5+0.2*(i-16)]
#     wp.append(temp)
# print(wp)
# print(len(wp))
# newdata = {'via_points':wp}
# new_path = os.path.join('/home/tanawatp/FRA501_61_WS/src/draw_fibo/via_point/via_point_'+'test_Humble.yaml')
# with open(new_path,'w') as file:
#     yaml.dump(newdata,file)