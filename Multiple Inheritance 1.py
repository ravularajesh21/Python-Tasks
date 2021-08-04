# Exm 1 :

class Bank:
    def __init__(self,employee,role):
        self.employee = employee
        self.role = role
    def Office(self):
        print('My name is',self.employee,'employee in this bank')
        print('Role is',self.role)   
class Bank2:
    def __init__(self, employee, role,experience,salary):
        super().__init__(employee, role)
        self.experience = experience
        self.salary = salary
    def Office2(self):
        print('Experience is',self.experience)
        print('Salary is',self.salary)
class Bank3(Bank2,Bank):
    def __init__(self, employee, role,experience,salary,Branch):
        super().__init__(employee, role,experience,salary)
        self.Branch = Branch
    def Office3(self):
        print('Branch is',self.Branch)
        
my = Bank3('Rajesh','Bank Manger',3,50000,'Jamikunta')
my.Office2()
my.Office3()

# Exm 2 :
    
class Bank1:
    def __init__(self,employee,role):
        self.employee = employee
        self.role = role
    def Office(self):
        print('My name is',self.employee,'employee in this bank')
        print('Role is',self.role)   
class Bank2:
    def __init__(self, employee, role,experience,salary):
        super().__init__(employee, role)
        self.experience = experience
        self.salary = salary
    def Office2(self):
        print('Experience is',self.experience)
        print('Salary is',self.salary)
class Bank3(Bank1,Bank3):
    def __init__(self, employee, role,experience,salary,Branch):
        super().__init__(employee, role)
        self.Branch = Branch
    def Office3(self):
        print('Branch is',self.Branch)
        
my = Bank3('Rajesh','Bank Manger',3,50000,'Jamikunta')
my.Office()
my.Office3()

# Exm 3 :
    
class A:
    a,b = 15,25
    def r1(self):
        a,b = 10,20
        print(a+b)
        print(self.a+self.b)
class B:
    c,d = 100,200
    def r2(self):
        c,d = 45,55
        print(c+d)
        print(self.c+self.d)
class C(A,B):
    e,f = 11,22
    def r3(self):
        e,f = 150,250
        print(e,f)
        print(self.e+self.f)

t = C()
t.r1()
t.r2()
t.r3()
      





