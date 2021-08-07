# Multi Threading:
    
# Exm 1 :

from threading import *

class raj(Thread):
    def ravi(self):
        for x in range(6):
            print('Child executing')
            
class rah(Thread):
    def ramu(self):
        for y in range(6):
            print('Hello')
            

t1 = raj()
t2 = rah()

t1.ravi()
t2.ramu()

# exm 2 :
    
from  threading import *
from time import sleep

class siva(Thread):
    def run(self):
        for x in range(6):
            print('hello')
            sleep(2)
class sriram(Thread):
    def run(self):
        for x in range(6):
            print('Hi')
            sleep(2)
t1 = siva()
t2 = sriram()

t1.start()
sleep(0.2)

t2.start()

# Exm 3 :
    
from  threading import *
from time import sleep

class siva(Thread):
    def run(self):
        for x in range(6):
            print('hello')
            sleep(1)
class sriram(Thread):
    def run(self):
        for x in range(6):
            print('Hi')
            sleep(1)
t1 = siva()
t2 = sriram()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print('Wecome to python development')












