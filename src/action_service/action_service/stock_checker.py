import rclpy
from rclpy.node import Node
from interfaces.srv import CheckStock
class StockCheckerServiceServer(Node):

    def __init__(self):
        super().__init__('stock_checker_service_server')
        self.stock_levels = {'book': 10, 'toy': 20, 'game': 5}  
        self.service_ = self.create_service(CheckStock, 'check_stock', self.check_stock_callback)

    def check_stock_callback(self, request, response):
        item_name = request.item_name
        if item_name in self.stock_levels:
            response.stock_level = self.stock_levels[item_name]
        else:
            response.stock_level = 0 
        return response

def main(args=None):
    rclpy.init(args=args)

    stock_checker_service_server = StockCheckerServiceServer()

    rclpy.spin(stock_checker_service_server)

if __name__ == '__main__':
    main()