import serial
import time

#seri port ayarlandi
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.0)

if (ser.isOpen() == False):
	ser.Open()
	print('port actim')

	
SMS='Selamin Aleykum Ben Omer'

ser.flushInput()

for i,c in enumerate(SMS):
	print("gonder:" + SMS[0:i])
	ser.write((SMS[0:i]+"\n"))
	time.sleep(0.1)
ser.close()
