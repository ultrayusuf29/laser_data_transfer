import serial
from multiprocessing import Process

ser=serial.Serial("/dev/serial0",baudrate=9600,timeout=1.0)
if (ser.isOpen()==False):
    ser.Open()
    print("Port açıldı.")
    
ser.flushInput()

def send_message():
    while 1:
        a=input("Mesajınızı girin:")
        if a=='':
            ser.write(a+"\n")
            print(a,' (Gönderildi)')
            
def receive_message():
    while 1:
        data=ser.readline()
        if data:
            print("\n alindi:\n"+data)
if __name__=='__main__':
    s=Process(target=send_message)
    r=Process(target=receive_message)
    s.start()
    r.start()
    s.join()
    r.join()
