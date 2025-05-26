# Diner Waitress Robot

**Diner Waitress Robot** adalah robot pelayan makanan yang dirancang untuk kebutuhan restoran menggunakan platform ROS 2. Robot ini mampu melakukan navigasi mandiri berbasis LiDAR dan menghindari rintangan secara real-time. Sistem ini dikembangkan dengan arsitektur modular agar dapat diintegrasikan dengan mikrokontroler eksternal (Arduino Mega) melalui komunikasi serial dua arah.

## 📦 Package Structure
diner_waitress_robot/
├── config/ # Konfigurasi SLAM, Navigation2, dan RViz
├── description/ # File URDF dan Xacro untuk model robot
├── launch/ # Launch file untuk SLAM, navigasi, dan sensor
├── CMakeLists.txt # Build configuration file
├── package.xml # ROS 2 manifest file
└── README.md # Dokumentasi paket

## 🔧 Fitur Utama

- Navigasi mandiri berbasis **SLAM Toolbox** dan **Nav2**
- Komunikasi serial dua arah dengan **Arduino Mega**
- Pemodelan robot lengkap menggunakan **URDF/Xacro**
- Visualisasi dan debugging dengan **RViz 2**
- Integrasi sensor **LiDAR** untuk mapping & obstacle avoidance

## 🚀 Cara Menjalankan

### 1. Build Workspace

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash

🔌 Dependencies
- ROS 2 Humble
- slam_toolbox
- Nav2
- rplidar_ros
- xacro, tf2, robot_state_publisher, joint_state_publisher