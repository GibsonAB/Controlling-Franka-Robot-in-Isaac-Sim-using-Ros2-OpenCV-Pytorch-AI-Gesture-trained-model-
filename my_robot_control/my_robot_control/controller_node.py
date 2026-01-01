import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from sensor_msgs.msg import JointState

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')

        self.sub = self.create_subscription(
            Int32,
            'gesture_id',
            self.gesture_callback,
            10
        )

        self.pub = self.create_publisher(
            JointState,
            'joint_command',
            10
        )

        self.joint_names = [
            'panda_joint1',
            'panda_joint2',
            'panda_joint3',
            'panda_joint4',
            'panda_joint5',
            'panda_joint6',
            'panda_joint7'
        ]

    def gesture_callback(self, msg: Int32):
        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = self.joint_names

        if msg.data == 1:
            js.position = [0.0, -0.5, 0.0, -2.0, 0.0, 1.5, 0.8]
        elif msg.data == 2:
            js.position = [0.3, -0.3, 0.2, -1.8, 0.2, 1.2, 0.5]
        elif msg.data == 3:
            js.position = [1.3, 0.8, 1.1, -2.2, 0.1, 1.8, 0.9]
        elif msg.data == 4:
            js.position = [1.1, -0.3, 0.9, -1.8, 0.2, 1.2, 0.5]
        elif msg.data == 5:
            js.position = [1.3, 2.8, 2.1, -2.2, 0.1, 1.8, 0.9]
        else:
            return  # ignore unknown gesture

        self.pub.publish(js)
        self.get_logger().info(f'Sent joint command for gesture {msg.data}')

def main():
    rclpy.init()
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
