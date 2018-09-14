import socket
import androidhelper
import time
import os 

path="/sdcard/a.wav"
if os.path.exists(path):
    os.remove(path)
 
droid=androidhelper.Android()

port=50000
s=socket.socket()
host="0.0.0.0"
s.bind((host,port))

while 1:
    s.listen(5)
    print("Server listening ...")
    conn,addr=s.accept()
    print("Got connection from",addr)
    data=conn.recv(1024)
    print("Server received:"+data)
    droid.recorderStartMicrophone("/sdcard/a.wav")
    print("Kayit Basladi")
    time.sleep(30)
    droid.recorderStop()
    print("Kayit Bitti")
    conn.send("YSF")
    f=open(path,"rb")
    l=f.read(1024)
    while (l):
        conn.send(l)
        l=f.read(1024)
    f.close()

    print("Recording and transferring done ..")
    conn.close()
    
    os.remove(path)
    
