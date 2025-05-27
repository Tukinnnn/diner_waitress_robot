from setuptools import setup

package_name = 'diner_waitress_bridge'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/serial_bridge.launch.py']),
        ('share/' + package_name + '/resource', ['resource/' + package_name])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='I Putu Kresna Dwipayana',
    maintainer_email='kresna@example.com',
    description='UART communication bridge between Jetson and Arduino for robot waitress.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_bridge_node = diner_waitress_bridge.serial_bridge:main',
        ],
    },
)
