class P:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Parl(self):
        print('Hello this is rajesh',self.name)
        print('iam',self.age,'old')
class C1(P):
    def __init__(self,name,age,role,experience):
        super().__init__(name, age)
        self.role = role
        self.experience = experience
    def Chill(self):
        print('My role is',self.role)
        print('I have',self.experience)
class C2(C1):
    def __init__(self,name,age,role,experience,salary,company):
        super().__init__(name, age, role, experience)
        self.salary = salary
        self.company = company
    def Cool(self):
        print('My salary is',self.salary)
        print('Im working in',self.company)
        
c = C2('Rajesh',26,'Python web developer','3years',50000,'Capgemini')
c.Parl()
c.Chill()
c.Cool()


      
        
