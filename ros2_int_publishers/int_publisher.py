# int_publisher.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import sys

class IntegerPublisher(Node):
    def __init__(self, value, topic):
        super().__init__('int_publisher')
        self.publisher_ = self.create_publisher(Int32, topic, 10)
        self.value = value
        self.topic = topic
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.value
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing {msg.data} on {self.topic}')

def main(args=None):
    rclpy.init(args=args)
    if len(sys.argv) != 3:
        print("Usage: int_publisher.py <value> <topic>")
        return

    value = int(sys.argv[1])
    topic = sys.argv[2]
    node = IntegerPublisher(value, topic)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
