from setuptools import find_packages, setup

package_name = 'action_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sami',
    maintainer_email='samitrad7@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'handle_items = action_service.handle_items:main',
            'item_delivery_action_client = action_service.Delivery_Action_Client:main',
            'stock_checker_service_client = action_service.Stock_Checker_Client:main',
            'stock_checker_service_server = action_service.stock_checker:main',
        ],
    },
)
