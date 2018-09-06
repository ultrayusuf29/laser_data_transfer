import serial
import time
from threading import Thread

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.0)
if (ser.isOpen() == False):
	ser.Open()
        print('port actim')
ser.flushInput()

def receive():
    while True:
	data = port.readline()
	if data:
		print ("\n alindi:\n"+data[:-1])
        time.sleep(0.1)
def transfer():
    for i,c in enumerate(SMS):
	print("gonder:" + SMS[0:i])
        ser.write((SMS[0:i]+"\n"))
        time.sleep(0.1)
    ser.close()

if __name__=='__main__':
    birinci=Thread(target=receiving)
    ikinci=Thread(target=transfer)

    birinci.start()
    ikinci.start()
