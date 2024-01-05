


> Written with [StackEdit](https://stackedit.io/).
> # FRA501_exam1_6461
> The draw_fibo package is a tool that, when invoked, spawns four turtles to draw the word "FIBO" by leaving a trail of pizza on the turtlesim_plus GUI. Each turtle has a specific name and role in the drawing process:
 - Foxy วาด F
 - Noetic วาด I
 - Humble วาด B
 - Iron วาด O

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
> [Click here : system architecture.png](https://drive.google.com/file/d/1BqTgiDabkhHZd-9FrFM0rYJEnVgUlL8M/view?usp=drive_link)
> 
> **Packages list**
 - *turtlesim_plus_planning* : เป็น package สำหรับสร้าง path ของเต่าเเต่ละตัวให้เป็นตัวอักษรที่ต้องการ โดยจะมี Node "*tao_plannig*" ที่จะสร้าง path สร้างตาม namespace เเละนำไปเก็บไว้ที่ via_point_xx.yaml ที่รับมาจาก ros parameters
 - *turtlesim_plus_scheduler* : เป็น package สำหรับจัดการตารางการเคลื่อนที่ของน้องเต่าโดยจะคอยบอกจุดต่อไปที่น้องเต่าต้องไป โดยจะมี Node "*tao_scheduler*" ทำการ request ผ่าน ros service "go2Target" นอกจากนี้ยังทำหน้าที่ในการส่ง request สำหรับการ spawn pizza อีกด้วยโดยภายใน package จะประกอบด้วย ros argument ที่เป็นการรับ file path ของ via_point_xx.yaml ที่อยู่ใน share directory
 - *turtlesim_plus_controller* : เป็น package สำหรับควบคุมให้น้องเต่าเคลื่อนที่ไปยังจุดที่ต้องการโดยใช้ P controller ภายในจะมี Node "*tao_controller*" ที่มีการประกาศ  ros parameters ไว้คือ kp_linear, kp_angular และ tolerance ซึ่งเมื่อถึงจุดหมายจะทำการส่ง request ผ่าน ros service "arriveFlag" เพื่อเป้นการบอก tao_scheduler ว่าถึงจุดหมายเเล้ว
 - *my_interface* : เป็น package ที่เอาไว้เก็บ  interfaces ที่ใช้ เช่น SetTarget
 - *draw_fibo* : เป็น package ที่เก็บไฟล์ launch, parameters.yaml เเละ via_points.yaml เอาไว้โดยใน launch จะประกอบไปด้วย 3 launch files ย่อย ได้เเก่ 
	 - spawn_4turtles.launch.py สำหรับการ spwan เต่าทั้ง 4 ตัวเเละตั้ง namespace ให้
	 - PCS.launch.py สำหรับสร้าง Node *tao_controller และ  tao_scheduler*รวมทั้งตั้ง namespace เเละนำ parameters, argument จากไฟล์ YAML  ไปใส่ไว้ที่ Node นั้น ๆ ด้วย
	 - draw.launch.py สำหรับเป็นตัว launch ของทั้ง 2 ไฟล์ด้านบนอีกที

> 
> ## Test and Run
> 1.)Sour your ROS2 and workspace
>
> 2.)go to FRA501_61_WS and enter this commands to launch
> 
> `	colcon build`
> 
> `	ros2 launch draw_fibo draw.launch.py`
>
> or you can run it separately
> 
> `ros2 launch draw_fibo spawn_4turtles.launch.py`
> 
> `ros2 launch draw_fibo PCS.launch.py`


write by : Tanawat


