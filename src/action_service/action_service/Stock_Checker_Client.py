import rclpy
from rclpy.node import Node

from interfaces.srv import CheckStock

class StockCheckerServiceClient(Node):
    def __init__(self):
        super().__init__('stock_checker_service_client')
        self.client = self.create_client(CheckStock, 'check_stock')

    def send_stock_check_request(self, item_name):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        request = CheckStock.Request()
        request.item_name = item_name

        future = self.client.call_async(request)

        future.add_done_callback(self.get_stock_level_callback)

    def get_stock_level_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Stock level for {response.item_name}: {response.stock_level}')
        except Exception as e:
            self.get_logger().error(f'Service call failed with error: {e}')

def main(args=None):
    rclpy.init(args=args)

    node = StockCheckerServiceClient()

    node.send_stock_check_request('book')

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()