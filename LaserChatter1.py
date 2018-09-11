import serial
from threading import Thread

ser=serial.Serial("/dev/pts/4",baudrate=9600,timeout=1.0)
if (ser.isOpen()==False):
    ser.Open()
    print("Port acildi.")
    
ser.flushInput()

def send_message(x):
        if x!='':
            ser.write(x+"\n")
            print(x,' (Gonderildi)')
            
def receive_message():
    while 1:
        data=ser.readline()
        if data:
            print("\n alindi:\n"+data)
if __name__=='__main__':
    r=Thread(target=receive_message)
    r.start()
    while 1:
        send_message(raw_input("Mesajinizi girin:"))

