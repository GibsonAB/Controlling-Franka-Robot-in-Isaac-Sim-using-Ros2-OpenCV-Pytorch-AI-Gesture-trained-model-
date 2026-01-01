from setuptools import find_packages, setup

package_name = 'my_robot_control'

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
    maintainer='gibson',
    maintainer_email='gibson@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'line_follower = my_robot_control.line_follower:main',
            'hand_gesture_node = my_robot_control.hand_gesture_node:main',
            'vision_navigation_node = my_robot_control.vision_navigation_node:main', 
            'controller = my_robot_control.controller:main',
            'path_planner = my_robot_control.path_planner:main',
            'gesture_node = my_robot_control.gesture_node:main',
            'controller_node = my_robot_control.controller_node:main',
            'collect_speed_data = my_robot_control.collect_speed_data:main',
            'train_speed_intent = my_robot_control.train_speed_intent:main',
            'speed_intent_live = my_robot_control.speed_intent_live:main'
            'AI_controller_node = my_robot_control.AI_controller_node:main',],
    },
)
