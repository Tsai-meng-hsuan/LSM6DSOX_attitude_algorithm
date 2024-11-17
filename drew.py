import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 設置串口連接
ser = serial.Serial('COM5', 9600, timeout=0.1)  # 這裡根據你的設備修改串口號

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

# 更新箭頭的函數
def update_arrow(acc_x, acc_y, acc_z):
    ax.cla()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.quiver(0, 0, 0, acc_x, acc_y, acc_z, color='r', label='Acceleration Vector')
    plt.draw()

plt.ion()
plt.show()

acc_x, acc_y, acc_z = [0,0,0]
while True:
    # 清除串口緩衝區
    ser.flushInput()  # 清除輸入緩衝區
    # ser.flushOutput()  # 清除輸出緩衝區
    # 從串口讀取加速度數據
    line = ser.readline().decode(errors='ignore').strip()  # 讀取一行並解碼為字符串
    
    try:
        acc_x, acc_y, acc_z = list(map(float, line.split(',')))
        # print(acc_x, acc_y, acc_z)
        # 更新箭頭
        update_arrow(acc_x, acc_y, acc_z)
        plt.pause(0.01)
    except:
        pass
    
    
