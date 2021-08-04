# Exm 1 :

class Bank:
    def __init__(self,employee,role,experience,salary,Branch):
        self.employee = employee
        self.role = role
        self.experience = experience
        self.salary = salary
        self.Branch = Branch
    def Office(self):
        print('My name is',self.employee,'employee in this bank')
        print('Role is',self.role)   
class Bank2(Bank):
    def Office2(self):
        print('Experience is',self.experience)
        print('Salary is',self.salary)
class Bank3(Bank):
    def Office3(self):
        print('Branch is',self.Branch)
        
my = Bank3('Rajesh','Bank Manger',3,50000,'Jamikunta')
my.Office()
my.Office3()

# Exm 2 :

class A:
    x,y = 10,15
    a,b = 500,1000
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b = 100,200
    def m2(self):
        print(self.a+self.b)
        print(super().x+super().y)
class C(A):
    i,j = 5,10
    def m3(self):
        print(self.i+self.j)
        print(super().a+super().b)
        print(A().x+A().y)
hi = C()
hi.m3()
hi.m1()
    
# exm 3 :
    
class A:
    x,y = 10,15
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b = 100,200
    def m2(self):
        print(self.a+self.b)
class C(A):
    i,j = 5,10
    def m3(self):
        print(self.i+self.j)
        print(B().a+B().b)
hi = C()
hi.m3()
hi.m1()