from threading import *
from time import sleep

class Info(Thread):
    
    def __init__(self):
        self.dob = self.DOB()
        self.address =self.Address()
        
    def fulldata(self):
        self.name = 'Rajesh'
        print('My name is ',self.name)
        sleep(2)
    class DOB(Thread):
        def __init__(self):
            self.dd = 26
            self.mm = 2
            self.yy = 1995
        def raju(self):
            print('DOB is {}/{}/{}'.format(self.dd,self.mm,self.yy))
            sleep(3)
    class Address(Thread):
        def __init__(self):
            self.city = 'Warangal'
            self.country = 'India'
        def Nari(self):
            print('I am from',self.city)
            print('My country is',self.country)
            sleep(3)
        

i = Info()
u = i.DOB()
o = i.Address()
i.fulldata()
u.raju()
o.Nari()
Info.DOB().raju()
Info.Address().Nari()