# Method overriding

class P1:
    def __init__(self,name,gender,age,place,interest):
        self.name = name
        self.gender = gender
        self.age = age
        self.place = place
        self.interest = interest
    def raj(self):
        print('My name is',self.name)
        print('Im',self.gender)
        print('Im',self.age,'old')
        print('Im interesting in',self.interest)
        print('Im from',self.place)
    def raj(self):
        print('Iam',self.name)
        print('my age is',self.age)
        print('Im from',self.place)
    def raj(self):
        
        print('My name is',self.name)
        print('Im',self.age,'old')

v = P1('Rajesh','Male','26','Warangal','3')
v.raj()

