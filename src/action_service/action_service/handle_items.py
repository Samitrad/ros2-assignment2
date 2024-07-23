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
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        item_name = goal_handle.request.item_name
        quantity = goal_handle.request.quantity

        
        status = 'Delivering...'
        for i in range(quantity):
            status = f'Delivering {i+1} of {quantity}...'
            goal_handle.publish_feedback(DeliverItem.Feedback(status))
            self.get_logger().info(status)
            rclpy.sleep(1)

        result = DeliverItem.Result()
        result.success = True
        result.message = f'Delivered {quantity} {item_name}(s) successfully!'
        return result

def main(args=None):
    rclpy.init(args=args)

    item_delivery_action_server = ItemDeliveryActionServer()

    rclpy.spin(item_delivery_action_server)

if __name__ == '__main__':
    main()