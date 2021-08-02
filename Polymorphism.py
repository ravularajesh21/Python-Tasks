# Overriding :

class Hari:
    'Hello every one'
    def __init__(self,name,age,gender,friend):
        self.name = name
        self.age = age
        self.gender = gender
        self.friend = friend
    def Raju(self):
        print('My name is',self.name)
        print('Im',self.age,'years old')
        print('Iam ',self.gender)
        print('My friend is',self.friend)
    def Raju(self):
        print('Iam ',self.gender)
        print('My friend is',self.friend)
hi = Hari('Rajesh',25,'Male','Satwik')
hi.Raju()


# Overloading :

class Hari:
    def __init__(self,name,age,gender,friend):
        self.name = name
        self.age = age
        self.gender = gender   # python does not support functional overloading
        self.friend = friend
    def Raju(self):
        print('My name is',self.name)
        print('Im',self.age,'years old')
    def Raju(self,cell,pin):
        print('Iam  ',self.cell)
        print('My friend is',self.pin)
        
hi = Hari('Rahul',35,'Male','Satwik')
hi.Raju()
hi.Raju(50000, 100)


