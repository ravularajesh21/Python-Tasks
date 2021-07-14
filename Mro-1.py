# Mro program-1

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print('My name is',self.name)
        print('Im',self.age)
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks
    def Chill(self):
        print('My rollno is',self.rollno)
        print('My marks',self.marks)
        
v = Student('Rajesh',25,13548,85)
v.display()
v.Chill()

# Mro program-2

class P:
    a = 10
    def __init__(self,ename,eno):
        self.b = 100
        self.ename = ename
        self.eno = eno
    def RS(self):
        print('Employee name is',self.ename)
        print('Employee Id no is',self.eno)
class R(P):
    a = 888
    def __init__(self, ename, eno,esal,ebranch):
        super().__init__(ename, eno)
        self.esal = esal
        self.ebranch = ebranch
    def SR(self):
        print('Employee Salary is',self.esal)
        print('Employee branch is',self.ebranch)
        print(super().a)
        print(self.b)
c = R('rajesh',123548,50000,'Hyderabad')
c.RS()
c.SR()

# Different approach
class p:
    a = 10
    def __init__(self):
        self.b = 100
    def m1 (self):
        print('this is first')
    def m2 (cls):
        print('this is second')
    def m3 (self):
        print('this is third')
class c(p):
    a = 888
    def __init__(self):
        self.b = 999
        super().__init__()
        print(super().a)
        print(self.a)
        print(self.b)
        print(self.b)
        super().m1()
        super().m2()
        super().m3()
        
c = c()