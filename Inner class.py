# Aproach 1:
class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Raj(self):
        print('This is',self.name)
        print('Im',self.age,'old')
    class B:
        def __init__(self,DOB,sal):
            self.DOB = DOB
            self.sal = sal
        def Raju(self):
            print('My date of birth is',self.DOB)
            print('My salary is',self.sal)
            
my = A('Rajesh',26)
my.Raj()
y = my.B("26-2-1995",50000)
y.Raju()


# Aproach 2:
    
class A:
    def __init__(self):
        pass
    class B:
        def __init__(self,DOB,sal):
            self.DOB = DOB
            self.sal = sal
        def Raju(self):
            print('My date of birth is',self.DOB)
            print('My salary is',self.sal)
            
my = A()

y = my.B("26-2-1995",50000)
y.Raju()


# Aproach 3:
    
class A:
    def __init__(self):
        self.db = self.DOB()
    class DOB:
        def __init__(self):
            self.dd = 26
            self.mm = 2
            self.yy = 1995
        def display(self):
            print('DOB = {}/{}/{}'.format(self.dd,self.mm,self.yy))
            
x = A()
y = x.DOB()
y.display()


# Aproach 4:

class Name:
    def __init__(self):
        self.name = 'Rajesh Khanna'
        self.db = self.DOB()
        self.place = self.City()
    def information(self):
        print('My name is',self.name)
    class DOB:
        def now(self):
            self.dd = 26
            self.mm = 2
            self.yy = 1995
            print('Date of Birth is = {}/{}/{}'.format(self.dd,self.mm,self.yy))
    class City:
        def Place(self):
            self.vlg = 'Bheempally'
            self.Mdl = 'Kamalapur'
            self.Dist = 'Hanamkonda'
            print('Home town is  {}'.format(self.vlg))
            print('My mondal is {}'.format(self.Mdl))
            print('My dist is {}'.format(self.Dist))
            
t = Name()
t.information()

u = t.DOB()
u.now()

g= t.City()
g.Place()


# Approach 5 :
  
class A:
    def __init__(self):
        self.db = self.Inner()
          
    def display(self):
        print('In Parent Class')
          
    # this is inner class
    class Inner:
              
        def display1(self):
            print('Inner Of Parent Class')
              
              
class B(A):
    def __init__(self):
        print('In Child Class')
        super().__init__()
          
    class Inner(A.Inner):
          
        def display2(self):
            print('Inner Of Child Class')
              
# creating child class object
p = B()
p.display()
  
# create inner class object
x = p.db
x.display1()
x.display2()


# Approch 6 :

class Doctors:
    def __init__(self):
        self.name = 'Doctor'
        self.den = self.Dentist()
        self.car = self.Cardiologist()
    def show(self):
        print('In outer class')
        print('Name:', self.name)
   
    class Dentist:  
        def __init__(self):
            self.name = 'Dr. Savita'
            self.degree = 'BDS'
        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)
   
    class Cardiologist:
        def __init__(self):
            self.name = 'Dr. Amit'
            self.degree = 'DM'
        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)
 

outer = Doctors()
outer.show()
  

d1 = outer.Dentist()
  
# create a object
# of 2nd inner class
d2 = outer.Cardiologist()
print()
d1.display()
print()
d2.display()
        