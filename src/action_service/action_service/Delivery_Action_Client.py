import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from interfaces.action import DeliverItem

class ItemDeliveryActionClient(Node):
    def __init__(self):
        super().__init__('item_delivery_action_client')
        self.action_client = ActionClient(self, DeliverItem, 'deliver_item')

    def send_delivery_request(self, item_name, quantity):
        goal_msg = DeliverItem.Goal()
        goal_msg.item_name = item_name
        goal_msg.quantity = quantity

        self.get_logger().info(f'Sending delivery request for {item_name}, quantity: {quantity}')
        self.action_client.wait_for_server()

        self.send_goal_future = self.action_client.send_goal_async(goal_msg)
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        if result:
            self.get_logger().info(f'Result: Success={result.success}, Message="{result.message}"')
        else:
            self.get_logger().error('No result received')

def main(args=None):
    rclpy.init(args=args)
    item_delivery_action_client = ItemDeliveryActionClient()
    item_delivery_action_client.send_delivery_request('book', 5)  # Example request
    rclpy.spin(item_delivery_action_client)
    item_delivery_action_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

