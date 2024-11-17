import serial

# 設置串行端口、波特率等參數
ser = serial.Serial('COM5', 9600)  # Windows下使用COM端口，Linux下使用/dev/ttyUSB0

# 一直讀取串行端口的資料
while True:
    while ser.in_waiting:          # 若收到序列資料…
        data_raw = ser.readline()  # 讀取一行
        data = data_raw.decode()   # 用預設的UTF-8解碼
        print(data_raw)
        print(data)
