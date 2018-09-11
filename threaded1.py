import serial
import time
from threading import Thread

ser = serial.Serial("/dev/pts/4", baudrate=9600, timeout=1.0)
if (ser.isOpen() == False):
	ser.Open()
        print('port actim')
ser.flushInput()
SMS="omer"
def receive():
    while True:
	data = ser.readline()
	if data:
		print ("\n alindi:\n"+data[:-1])
        time.sleep(0.1)
def transfer():
        while 1:
            for i,c in enumerate(SMS):
                print("gonder:" + SMS[0:i])
                ser.write((SMS[0:i]+"\n"))
                time.sleep(0.1)


if __name__=='__main__':
    birinci=Thread(target=receive)
    ikinci=Thread(target=transfer)

    birinci.start()
    ikinci.start()
