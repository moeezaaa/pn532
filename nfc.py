import serial
import time

# Ganti 'COMx' dengan port serial Arduino yang terhubung
ser = serial.Serial('COMx', 115200, timeout=1)

def unlock_screen():
    print("Screen unlocked!")
    # Tambahkan logika untuk menyalakan layar di sini

def lock_screen():
    print("Screen locked!")
    # Tambahkan logika untuk mengunci layar di sini

while True:
    data = ser.read().decode('utf-8')
    if data:
        if data == 'U':
            unlock_screen()
        elif data == 'L':
            lock_screen()

    time.sleep(0.1)
