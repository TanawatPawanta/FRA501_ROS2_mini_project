#!/usr/bin/python3

from turtlesim_plus_scheduler.dummy_module import dummy_function, dummy_var
import rclpy
import argparse
import yaml
from rclpy.node import Node
from my_interfaces.srv import SetTarget, ImDone
from turtlesim_plus_interfaces.srv import GivePosition
from std_srvs.srv import Empty

class Scheduler(Node):
    def __init__(self, file_path:str):
        super().__init__('tao_scheduler')
        # creat service server
        self.create_service(srv_type=Empty,srv_name="arriveFlag",callback=self.arriveFlag_callback)
        # create service client
        self.go2target_cli = self.create_client(srv_type=SetTarget,srv_name="go2Target")
        self.spawnPizzaCli = self.create_client(GivePosition,"/spawn_pizza")
        self.create_timer(0.01,self.timer_callback)
        # local variables
        self.clock = 0.0
        self.vp_ind = 0
        self.state = "drawing"
        with open(file_path,'r') as file:
            data = yaml.load(file, Loader=yaml.SafeLoader)
        self.via_points = data['via_points']
        self.num = len(self.via_points)
        # self.send_target(self.via_points[self.vp_ind])
    # ========================class's methodes===============================
    def timer_callback(self):
        self.clock += 0.01
        match self.state:
            case "init":
                if(self.clock >= 0.5 ):
                    self.state = "drawing"
                    self.send_target(self.via_points[self.vp_ind])
        #     case "drawing":
        #         pass
        #     case "done":
        #         pass

    def send_target(self,pos:list):
        tar_req = SetTarget.Request()
        tar_req.target.x = pos[0]
        tar_req.target.y = pos[1]
        self.go2target_cli.call_async(tar_req)

    def arriveFlag_callback(self, request, response):
        # if(request.success):
        # pos = [request.imhere.x, request.imhere.y]
        if(self.state == "drawing"):
            self.pizza_spawn(self.via_points[self.vp_ind])

        if(self.vp_ind + 1 < self.num):
            self.vp_ind = self.vp_ind+1
            self.send_target(self.via_points[self.vp_ind])
        else:
            self.send_target([9.0, 9.0])
            self.state = "done"
        return response
    def pizza_spawn(self, pos:list):
        pos_req = GivePosition.Request()
        pos_req.x = pos[0]
        pos_req.y = pos[1]
        self.spawnPizzaCli.call_async(pos_req)

def main(args=None):
    parser = argparse.ArgumentParser(description='schedule via point')
    parser.add_argument('-f','--file',help='path to YAML via point')
    parsed_args, remaining_args = parser.parse_known_args(args=args)

    rclpy.init(args=remaining_args)
    vp_filepath = parsed_args.file
    node = Scheduler(vp_filepath)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
