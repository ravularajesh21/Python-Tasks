# From Server Program

from socket import *

def Hari():
    host = gethostbyname()
    portno = 8088
    s = socket()
    s.bind(host,portno)
    print('server is running')
    s.listen()
    c,ad = s.accept()
    print('connection established')
    msg = c.recv()
    print(msg)
    c.send(b,'Hello client')
    s.close()
    
Hari()


# From Client Program


from socket import *

def Mahi():
    host = gethostbyname()
    portno = 8088
    s = socket()
    s.connect((host,portno))
    s.send(b,'Hello server')
    msg = s.recv(1024)
    print(msg)
    s.close()
    
Hari()
    
Mahi()