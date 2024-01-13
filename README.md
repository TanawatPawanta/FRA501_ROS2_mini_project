


> Written with [StackEdit](https://stackedit.io/).
> # FRA501_exam1_6461
> The draw_fibo package is a tool that, when invoked, spawns four turtles to draw the word "FIBO" by leaving a trail of pizza on the turtlesim_plus GUI. Each turtle has a specific name and role in the drawing process:
 - Foxy 	draw F
 - Noetic 	draw I
 - Humble 	draw B
 - Iron 	draw O

> ## Table of contents
> 
 - [Installation](#installation)
 - [System Architecture](#system-architecture)
 - [Test and Run](#test-and-run)
> ## Installation
> 1.) open terminal and enter this command in yor terminal
> 
> `git clone https://github.com/Fzil0n/FRA501_exam1_6461.git`
>
> 2.) go to FRA501_61_WS/src and enter this command
> 
> `git clone https://github.com/tchoopojcharoen/turtlesim_plus.git`
> 
> ## System Architecture
> 
> <img width="562" alt="image" src="https://github.com/TanawatPawanta/FRA501_ROS2_mini_project/assets/83177015/a69990fb-6c47-4aff-a61e-3f51678ad5e4">
> 
> **Packages list**
 - *turtlesim_plus_planning* : This is a package for generating paths for each turtle to follow based on the desired characters. It includes a node "tao_planning" that creates paths according to the specified namespace and stores them in via_point_xx.yaml files, which are received from ROS parameters.
 - *turtlesim_plus_scheduler* : This is a package for managing the movement schedule of the turtles. It informs each turtle about the next point it should move to. The package includes a node "tao_scheduler" that requests this information through the ROS service "go2Target". Additionally, it plays a role in sending requests for pizza spawning. Inside the package, there are ROS arguments that receive file paths for via_point_xx.yaml files located in the share directory.
 - *turtlesim_plus_controller* : This is a package for controlling the movement of turtles to specific points using a P controller. Inside, there is a node "tao_controller" that declares ROS parameters, namely kp_linear, kp_angular, and tolerance. When the turtle reaches its destination, it sends a request through the ROS service "arriveFlag" to inform the tao_scheduler that it has reached the target point.
 - *my_interface* : This is a package for store interfaces that used in this project such as SetTarget.
 - *draw_fibo* : This is a main package in this package contain launch file, parameters.yaml and via_points.yaml, in the launch folder have 3 sub launch files:  
	 - spawn_4turtles.launch.py for spwan 4 tuetles and set their namespace.
	 - PCS.launch.py for creat Node *tao_controller and  tao_scheduler*,set node's namespace.
	 - draw.launch.py for launch 2 file above.

> 
> ## Test and Run
> 
1.)Source your ROS2 and workspace
>
2.)go to FRA501_61_WS and enter this commands to launch
> 
> `colcon build`
> 
> `ros2 launch draw_fibo draw.launch.py`
>
> or you can run it separately
> 
> `ros2 launch draw_fibo spawn_4turtles.launch.py`
> 
> `ros2 launch draw_fibo PCS.launch.py`





