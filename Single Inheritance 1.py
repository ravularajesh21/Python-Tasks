# Single Inheritance

# exm 1 :

class Employee:
    a = 333

class Work(Employee):
    b = 1000
pr = Work()
print(pr.a)
print(pr.b)

# exm 2 :

class Employee:
    def __init__(self,name,role,experience):
        self.name = name
        self.role = role
        self.experience = experience
    def Office(self): 
        print('Employee Name is',self.name)
        print('Employee role is',self.role)
        print('I have',self.experience,'years experience')
        
class Work(Employee):
    def Office(self):
        print('I have',self.experience,'years experience')
        

pr = Work('Rajesh','Python','Developer')
pr.Office()

# exm 3 :

class Employee:
    def __init__(self,name,role,experience):
        self.name = name
        self.role = role
        self.experience = experience
    def Office1(self): 
        print('Employee Name is',self.name)
        print('Employee role is',self.role)
        print('I have',self.experience,'years experience')
        
class Work(Employee):
    def Office2(self):
        print('I have',self.experience,'years experience')
        

pr = Work('Rajesh','Python','Developer')
pr.Office2()
pr.Office1()



