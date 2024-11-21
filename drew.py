import serial
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 定義旋轉矩陣：繞 x 軸旋轉
def rotation_matrix_x(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

# 定義旋轉矩陣：繞 y 軸旋轉
def rotation_matrix_y(theta):
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

# 定義旋轉矩陣：繞 z 軸旋轉
def rotation_matrix_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])


# 更新箭頭的函數
def update_arrow(angle_x, angle_y, angle_z):
    ax.cla()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    vector_x = np.array([[1],[0],[0]])
    vector_y = np.array([[0],[1],[0]])
    vector_z = np.array([[0],[0],[1]])
    vector_x = rotation_matrix_x(angle_x) @ rotation_matrix_y(angle_y) @ rotation_matrix_z(angle_z) @ vector_x
    vector_y = rotation_matrix_x(angle_x) @ rotation_matrix_y(angle_y) @ rotation_matrix_z(angle_z) @ vector_y
    vector_z = rotation_matrix_x(angle_x) @ rotation_matrix_y(angle_y) @ rotation_matrix_z(angle_z) @ vector_z
    vector_x_x, vector_x_y, vector_x_z = vector_x.flatten().tolist()
    vector_y_x, vector_y_y, vector_y_z = vector_y.flatten().tolist()
    vector_z_x, vector_z_y, vector_z_z = vector_z.flatten().tolist()

    ax.quiver(0, 0, 0, vector_x_x, vector_x_y, vector_x_z, color='r', label='Acceleration Vector')
    ax.quiver(0, 0, 0, vector_y_x, vector_y_y, vector_y_z, color='g', label='Acceleration Vector')
    ax.quiver(0, 0, 0, vector_z_x, vector_z_y, vector_z_z, color='b', label='Acceleration Vector')
    plt.draw()

# 設置串口連接
ser = serial.Serial('COM8', 9600, timeout=0.1)  # 這裡根據你的設備修改串口號

# 初始化圖形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 設置坐標軸範圍
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.ion()
plt.show()


angle_x, angle_y, angle_z = [0,0,0]
before_time = time.time()
while True:
    # 清除串口緩衝區
    ser.flushInput()  # 清除輸入緩衝區
    # ser.flushOutput()  # 清除輸出緩衝區
    # 從串口讀取加速度數據
    line = ser.readline().decode(errors='ignore').strip()  # 讀取一行並解碼為字符串
    try:
        delta_angle_x, delta_angle_y, delta_angle_z = list(map(float, line.split(',')))
        after_time = time.time()
        delta_time = after_time - before_time
        before_time = time.time()
        angle_x += delta_time*delta_angle_x
        angle_y += delta_time*delta_angle_y
        angle_z += delta_time*delta_angle_z
        # print(angle_x, angle_y, angle_z)
        
        # 更新箭頭
        update_arrow(angle_x, angle_y, angle_z)
        plt.pause(0.01)
    except:
        continue
    
    
