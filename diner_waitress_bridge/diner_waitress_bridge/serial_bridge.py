# diner_waitress_bridge/serial_bridge.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import threading

from diner_waitress_bridge.parser import parse_message, is_valid_command
from diner_waitress_bridge.command_definitions import make_command, is_acknowledged, is_error

class SerialBridgeNode(Node):
    def __init__(self):
        super().__init__('serial_bridge_node')

        # Parameter koneksi serial
        self.declare_parameter('port', '/dev/ttyUSB0')
        self.declare_parameter('baudrate', 115200)
        self.declare_parameter('timeout', 1.0)

        port = self.get_parameter('port').get_parameter_value().string_value
        baudrate = self.get_parameter('baudrate').get_parameter_value().integer_value
        timeout = self.get_parameter('timeout').get_parameter_value().double_value

        # Inisialisasi serial
        try:
            self.serial_conn = serial.Serial(port, baudrate, timeout=timeout)
            self.get_logger().info(f"✅ Serial connected to {port} @ {baudrate}bps")
        except serial.SerialException as e:
            self.get_logger().error(f"❌ Gagal membuka serial port: {e}")
            raise e

        # ROS publisher dan subscriber
        self.pub_from_arduino = self.create_publisher(String, 'from_arduino', 10)
        self.sub_to_arduino = self.create_subscription(String, 'to_arduino', self.send_to_arduino_callback, 10)

        # Jalankan thread pembaca serial
        self.serial_thread = threading.Thread(target=self.read_serial_loop, daemon=True)
        self.serial_thread.start()

    def send_to_arduino_callback(self, msg):
        """Kirim command dari ROS ke Arduino."""
        try:
            command_str = msg.data.strip()
            self.serial_conn.write((command_str + '\n').encode('utf-8'))
            self.get_logger().info(f"[TX] → {command_str}")
        except Exception as e:
            self.get_logger().error(f"[TX ERROR] {e}")

    def read_serial_loop(self):
        """Loop untuk membaca data dari Arduino."""
        while rclpy.ok():
            try:
                if self.serial_conn.in_waiting:
                    line = self.serial_conn.readline().decode('utf-8').strip()
                    if line:
                        parsed = parse_message(line)
                        if is_valid_command(parsed):
                            if is_acknowledged(parsed):
                                self.get_logger().info(f"[ACK] Arduino acknowledged command")
                            elif is_error(parsed):
                                self.get_logger().warn(f"[ERR] Arduino error reported")

                        msg = String()
                        msg.data = line
                        self.pub_from_arduino.publish(msg)
                        self.get_logger().info(f"[RX] ← {line}")
            except Exception as e:
                self.get_logger().warn(f"[Serial Error] {e}")
                break

def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = SerialBridgeNode()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node and node.serial_conn.is_open:
            node.serial_conn.close()
        if node:
            node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
