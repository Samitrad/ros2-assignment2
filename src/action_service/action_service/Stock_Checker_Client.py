import rclpy
from rclpy.node import Node

from interfaces.srv import CheckStock
import matplotlib.pyplot as plt

class StockCheckerServiceClient(Node):
    def __init__(self):
        super().__init__('stock_checker_service_client')
        self.client = self.create_client(CheckStock, 'check_stock')
        self.stock_levels = {}  # Store stock levels for plotting

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
            self.stock_levels[response.item_name] = response.stock_level
            self.plot_stock_levels()
            self.get_logger().info(f'Stock level for {response.item_name}: {response.stock_level}')
        except Exception as e:
            self.get_logger().error(f'Service call failed with error: {e}')

    def plot_stock_levels(self):
        plt.figure(figsize=(8, 6))
        plt.bar(self.stock_levels.keys(), self.stock_levels.values())
        plt.xlabel("Item")
        plt.ylabel("Stock Level")
        plt.title("Stock Levels")
        plt.grid(True)
        plt.show()

def main(args=None):
    rclpy.init(args=args)

    node = StockCheckerServiceClient()

    item_names = ["book", "pen", "paper"]  # Replace with your desired items
    for item in item_names:
        node.send_stock_check_request(item)

    rclpy.spin(node)

    plt.close('all')  # Close all plots
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
