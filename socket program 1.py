# Server Program :

from socket import *

def main():
    host = gethostname()
    port = 8088
    s=socket()
    s.bind((host,port))
    print('Hello')
    s.listen(5)
    c,add = s.accept()
    c.send(b'Hello Ravula')
    msg = c.recv(1024)
    print(msg)
    
    
main()     


# Client Program :

from socket import *

def main():
    host = gethostname()
    port = 8088
    s = socket()
    s.connect((host,port))
    s.send(b'Hello Rajesh')
    msg = s.recv(1024)
    print(msg)
    s.close()
    
main()
