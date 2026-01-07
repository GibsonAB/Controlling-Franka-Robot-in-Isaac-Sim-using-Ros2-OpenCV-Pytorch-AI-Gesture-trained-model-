# Controlling-Franka-Robot-in-Isaac-Sim-using-Ros2-OpenCV-Pytorch-AI-Gesture-trained-model-
https://github.com/user-attachments/assets/6e050375-f4b9-4bba-b913-454a7a25524d
# Gesture-Controlled Franka Robot (ROS2 + Isaac Sim)

This project implements a **gesture-controlled Franka Panda robot** using **ROS2** and **NVIDIA Isaac Sim**.  
Human hand gestures are used to command the robot to move to predefined target configurations in simulation.

The system is designed with a **modular robotics architecture**, enabling future integration of **AI-based speed and intent estimation**.

---

## Features

- Hand gesture recognition using OpenCV
- ROS2-based modular control pipeline
- Position + velocity control of Franka Panda
- Real-time interaction in Isaac Sim
- Clean separation between perception, decision, and control
- AI-based speed-intent estimation (**planned**)

---

## System Architecture
Camera
->
Hand Gesture Node (OpenCV)
->
gesture_id (ROS2 topic)
->
Controller Node
->
JointState (position + velocity)
->
Isaac Sim (Franka Panda)

Now currently implementing basic industrial process instead of targets and trying to initial each sub-process with hand gestures.


