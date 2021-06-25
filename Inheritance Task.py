# Inheritance Task

a,b = 88,66

class A:
    a,b = 10,20 
    
class B(A):
    a,b = 150,250
    def ts(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])
        print(super().a+super().b)
        print(A().a+A().b)
class C(B):
    def ts1(self):
        print(super().a) # immediate parent
        print(A().a)   #First parent
    
b1=C() 
b1.ts1()
#import time
#print(time.cytime())       
        
       
        