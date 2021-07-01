# Multi Threading

# Approach 1

from threading import *
from time import sleep

class Raju(Thread):
    def run (self):
        for x in range(1):
            print('Tarun')
            sleep(2)
class Mohan(Thread):
    def Umesh (self):
        for x in range(5):
            print('sriram')

T1 = Raju()
T2 = Mohan()   

T1.run()
T2.Umesh()

# Approach 2


from threading import *
from time import sleep

class A(Thread):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Hani(self):
        print(self.name)
        print(self.age)
        sleep(2)
class C(Thread):
    def Best(self,place,gender):
        self.place = place
        self.gender = gender
        print(self.place)
        print(self.gender)
H1 = A('rajesh',25)
H1.Hani()
H = C()
H.Best('warnagal','Male')


       