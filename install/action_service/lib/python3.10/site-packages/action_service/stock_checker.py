import rclpy
from rclpy.node import Node
from interfaces.srv import CheckStock

class StockCheckerServiceServer(Node):

    def __init__(self):
        super().__init__('stock_checker_service_server')
        # Sample stock levels for testing
        self.stock_levels = {'book': 10, 'pen': 20, 'game': 5}  
        self.service_ = self.create_service(CheckStock, 'check_stock', self.check_stock_callback)
        self.get_logger().info('StockCheckerServiceServer initialized.')

    def check_stock_callback(self, request, response):
        item_name = request.item_name
        self.get_logger().info(f'Received request for item: {item_name}')
        if item_name in self.stock_levels:
            response.stock_level = self.stock_levels[item_name]
        else:
            response.stock_level = 0  # Item not found
        self.get_logger().info(f'Stock level for {item_name}: {response.stock_level}')
        return response

def main(args=None):
    rclpy.init(args=args)
    stock_checker_service_server = StockCheckerServiceServer()
    rclpy.spin(stock_checker_service_server)
    stock_checker_service_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
