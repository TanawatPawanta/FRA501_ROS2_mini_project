#!/usr/bin/python3

from turtlesim_plus_planning.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
import yaml

class Planning(Node):
    def __init__(self):
        super().__init__('tao_planning')
        self.declare_parameter('namespace',None)
        self.declare_parameter('new_file_path',None)
        self.via_points_packing()
    # class's method
    def via_points_packing(self):
        ns = self.get_parameter('namespace').value
        wp = []
        match ns:
            case 'Foxy': #F
                wp = self.gen_F()
            case 'Noetic': #I
                wp = self.gen_I()
            case 'Humble': #B
                wp = self.gen_B()
            case 'Iron' : #O
                wp = self.gen_O()
        newdata = {'via_points':wp}
        new_path = self.get_parameter('new_file_path').value
        with open(new_path,'w') as file:
            yaml.dump(newdata,file)

    def gen_F(self)->list:
        wp = []
        for i in range(20):
            if(i<10):
                temp = [1.5,6+0.3*i]
            elif(i>=10 and i<15):
                temp = [1.5+0.2*(i-9),9.0]        
            else:
                temp = [1.5+0.2*(i-15),8.0]
            wp.append(temp)
        return wp
    def gen_I(self)->list:
        wp = []
        for i in range(20):
            if(i<10):
                temp = [5.0,6+0.2*i]
            elif(i>=10 and i<15):
                temp = [4.5+0.2*(i-9),8.0]        
            else:
                temp = [4.5+0.2*(i-15),6.0]
            wp.append(temp)
        return wp
    def gen_B(self)->list:
        wp=[]
        for i in range(20):
            # if(i<8):
            #     temp = [1.5,3.5+0.2*i]
            # elif(i>=8 and i<11):
            #     emp = [1.5+0.2*(i-7),5.1-0.1*(i-7)]
            # elif(i>=12 and i<14):
            #     temp = [1.5+0.2*(i-10),4.3+0.1*(i-10)]
            # elif(i>=14 and i<16):
            #     temp = [1.5+0.2*(i-13),4.3-0.1*(i-13)]
            # else:
            #     temp = [1.5+0.2*(i-16),3.5+0.1*(i-16)]
            if(i<9):
                temp = [1.5, 2.0+0.2*i]
            elif(i>=9 and i<13):
                temp = [1.5+0.2*(i-8), 2.8]
            elif(i>=13 and i<17):
                temp = [2.3, 2.8-0.2*(i-12)]
            else:
                temp = [2.3-0.2*(i-16), 2.0]
            wp.append(temp)
        return wp
    def gen_O(self)->list:
        wp = []
        for i in range(20):
            if(i<5):
                temp = [4.5+0.2*i,3.5]
            elif(i>=5 and i<10):
                temp = [4.5,4.5-0.2*(i-4)]
            elif(i>=10 and i<16):
                temp = [5.5,3.5+0.2*(i-9)]
            else:
                temp = [5.5-0.2*(i-15),4.5]
            wp.append(temp)
        return wp

def main(args=None):
    rclpy.init(args=args)
    node = Planning()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
