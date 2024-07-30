import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from interfaces.action import DeliverItem

class ItemDeliveryActionServer(Node):
    def __init__(self):
        super().__init__('item_delivery_action_server')
        self._action_server = ActionServer(
            self,
            DeliverItem,
            'deliver_item',
            self.execute_callback
        )
        self.get_logger().info('ItemDeliveryActionServer initialized.')

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        item_name = goal_handle.request.item_name
        quantity = goal_handle.request.quantity

        # Immediately send the result without any delay
        result = DeliverItem.Result()
        if quantity <= 0:
            result.success = False
            result.message = f'Invalid quantity {quantity} for item {item_name}.'
            goal_handle.abort()  # Abort the goal if quantity is invalid
        else:
            result.success = True
            result.message = f'Successfully delivered {quantity} {item_name}(s).'
            quantity -=1
            goal_handle.succeed()  # Complete the goal successfully
        
        self.get_logger().info(result.message)
        return result

def main(args=None):
    rclpy.init(args=args)
    item_delivery_action_server = ItemDeliveryActionServer()
    rclpy.spin(item_delivery_action_server)
    item_delivery_action_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

