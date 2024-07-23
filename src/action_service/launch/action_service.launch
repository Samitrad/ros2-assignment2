import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    handle_items_node = Node(
        package='action_service',
        executable='handle_items',  
        name='node1',
        output='screen'
    )
    
    stock_checker_service_server_node = Node(
        package='action_service',
        executable='stock_checker_service_server',  
        name='node2',
        output='screen'
    )
    
    item_delivery_action_client_node = Node(
        package='action_service',
        executable='item_delivery_action_client', 
        name='node3',
        output='screen'
    )
    
    stock_checker_service_client_node = Node(
        package='action_service',
        executable='stock_checker_service_client', 
        name='node4',
        output='screen'
    )
    
    return LaunchDescription([
        handle_items_node,
        stock_checker_service_server_node,
        item_delivery_action_client_node,
        stock_checker_service_client_node
    ])

