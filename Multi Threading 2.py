# Without creating a class

# Aproach 1:
    

def raju():
    for x in range(6):
        print('Hello Ravula')
def ragu():
    for x in  range(6):
        print('Kothapalli')
        
t1 = Thread(target=raju)
t2 = Thread(target = ragu)

t1.start()
t2.start()

# Aproach 2:
    

from time import sleep

def raju():
    for x in range(6):
        print('Hello Ravula')
        sleep(1)
        
def ragu():
    for x in  range(6):
        print('Kothapalli')
        sleep(1)

t1 = Thread(target=raju)
t2 = Thread(target = ragu)

t1.start()
sleep(0.2)
t2.start()

# To know current thread

from threading import *
from time import sleep
def raju():
    for x in range(6):
        print('Hello Ravula....',current_thread().getName())
        sleep(1)
def ragu():
    for x in  range(6):
        print('Kothapalli...',current_thread().getName())
        sleep(1)

t1 = Thread(target=raju)
t2 = Thread(target = ragu)

t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print('Bye..',current_thread().getName())

# By Extend the thread class

from threading import *
from time import sleep
class raju(Thread):
    def run(self):
        for x in range(6):
            print('Hello Ravula')
            sleep(1)
class ragu(Thread):
    def run(self):
        for x in range(6):
            print('Kothapally')
            sleep(1)
            
t1 = raju()
t2 = ragu()

t1.start()
t2.start()

# Without extending Thread class

from threading import *
from time import sleep
class raju(Thread):
    def rani(self):
        list1 = [10,'Hi',25,40,'Bah']
        for x in list1:
            print('Hello Ravula',x)
            sleep(1)
class ragu(Thread):
    def ramu(self):
        list1 = [25,'Hello',35,55,'Bahu']
        for x in list1:
            print('Kothapally',x)
            sleep(1)
            
s1 = raju()
t1 = Thread(target = s1.rani)

s2 = ragu()
t2 = Thread(target = s2.ramu)

t1.start()
sleep(0.2)
t2.start()


# Time Comparision

import time

def rani(n):
   for x in n:
       time.sleep(1)
       print(x%2)
def ramu(n):
   for x in n:
       time.sleep(1)
       print(x%3)
                  
n = [2,4,3,6,7]
s = time.time()
rani(n)
ramu(n)
e = time.time()
print(e-s)


# If we want including threads

from threading import *
import time

def rani(n):
   for x in n:
       time.sleep(1)
       print(x%2)
def ramu(n):
   for x in n:
       time.sleep(1)
       print(x%3)
                  
n = [2,4,3,6,7]
s = time.time()
t1 = Thread(target = rani,args = (n,))
t2 = Thread(target = ramu,args = (n,))

t1.start()
t2.start()
t1.join()
t2.join()
e = time.time()
print(e-s)























