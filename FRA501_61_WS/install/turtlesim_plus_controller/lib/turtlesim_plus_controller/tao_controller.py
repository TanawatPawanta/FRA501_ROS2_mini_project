#!/usr/bin/python3

# from turtlesim_plus_controller.dummy_module import dummy_function, dummy_var
import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from my_interfaces.srv import SetTarget, ImDone
from std_srvs.srv import Empty

class Controller(Node):
    def __init__(self):
        super().__init__('tao_controller')
        # declear parameters
        self.declare_parameter('kp_linear',5.0)
        self.declare_parameter('kp_angular',5.0)
        self.declare_parameter('tolerance',0.1)
        # create publishers and subscribers
        self.pose_topic = self.get_namespace()+'/pose'
        self.create_subscription(Pose,self.pose_topic,self.pose_callback,10)
        self.pub_cmdvel = self.create_publisher(Twist,"cmd_vel",10)
        # create service server
        self.create_service(SetTarget,"go2Target",self.go2target_callback)
        # create service client
        self.arriveFlag_cli = self.create_client(srv_type=Empty,srv_name='arriveFlag')
        # create timer
        self.create_timer(0.01,self.timer_callback)
        # local variables
        self.currentPose = [0.0, 0.0, 0.0]
        self.targetPose = [0.0, 0.0, 0.0]
        self.targetTheta = 0.0
        self.control_enable = 0
    # ===========================class's methodes ===============================================
    def pose_callback(self, msg):
        self.currentPose[0] = msg.x
        self.currentPose[1] = msg.y
        self.currentPose[2] = msg.theta
    def cmd_vel(self, vx:float, w:float)->None:
        cmd_vel = Twist()
        cmd_vel.linear.x = vx
        cmd_vel.angular.z = w
        self.pub_cmdvel.publish(cmd_vel)
    def timer_callback(self):
        if self.control_enable == 0:
            self.cmd_vel(0.0,0.0)
        else:
            kp_l = self.get_parameter('kp_linear').value
            kp_a = self.get_parameter('kp_angular').value
            tol = self.get_parameter('tolerance').value
            dx = self.targetPose[0] - self.currentPose[0]
            dy = self.targetPose[1] - self.currentPose[1]
            self.targetTheta = math.atan2(dy, dx)
           
            d = math.hypot(dx,dy)
            if(d < tol):
                self.control_enable = 0
                # self.cmd_vel(0.0,0.0)
                self.tell_imArrive()
            else:
                uw = kp_a*(self.targetTheta - self.currentPose[2])
                uvx = kp_l*(d)
                self.cmd_vel(uvx, uw)

    def go2target_callback(self, request, response):
        if(self.control_enable==1):
            response.result = False
        else:
            response.result = True
            self.targetPose = [request.target.x,request.target.y,0.0]
            self.cmd_vel(0.0,0.0)
            self.control_enable = 1
        return response
    def tell_imArrive(self):
        arrive_req = Empty.Request()
        # arrive_req.success = True
        # arrive_req.imhere.x = self.currentPose[0]
        # arrive_req.imhere.y = self.currentPose[1]
        self.arriveFlag_cli.call_async(arrive_req)

def main(args=None):
    rclpy.init(args=args)
    node = Controller()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
