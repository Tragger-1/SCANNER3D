
import serial,time


def Serialstart(ser):
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)
    ser.flush()
    return ser

def SerialEnvoi(message,ser):

    #ser.write(message.decode(encoding='utf-8', errors='ignore'))
    ser.write(message)
    