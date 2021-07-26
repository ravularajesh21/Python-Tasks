# Lambda Functions

# A lambda function can take any number of arguments, but can only have one expression.
# They are mostly used along with map and filter functions


# Filter function

# Normal function
def value(n):
    print(n**2)
n = int(input('enter number:'))
value(n)

# Lambda functions
value = lambda n:n**2
print(value(4))

# adding multiple numbers
add = lambda x,y,z:x + y + z
print(add(10,20,30))

# filter function()

# syntax ---->
# filter(function,sequence)

# Using filter without lambda function 
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
list1 = [0,5,10,15,20]
output = list(filter(is_even,list1))
print(output)   


# Using filter with lambda function 

list1 = [0,5,10,15,20,25,30,35,40]
even = list(filter(lambda n:n%2==0,list1))
odd = list(filter(lambda n: n%2!=0,list1))
print(even)
print(odd)


tuple1 = ('A','AA','AAA','AAAA','AAAAA','AAAAAA','AAAAAAA')
tuple2 = list(filter(lambda s:len(s)<=4,tuple1))
tuple3 = list(filter(lambda s:len(s)>=4,tuple1))
print(tuple2)
print(tuple3)

# Example 1:

class employee:
    def __init__(self,name,sal,age,has_gf):
        self.name = name
        self.sal = sal
        self.age = age
        self.has_gf = has_gf
    def display(self):
        return self.name
e1 = employee('durga',20000,60,True)
e2 = employee('Ravi',4000,23,True)
e3 = employee('Shiva',2000,60,False)
e4 = employee('Pavan',5000,20,True)
e5 = employee('Kiran',50000,60,True)
e6 = employee('Teja', 60000, 22, True)

list1 = [e1,e2,e3,e4,e5,e6]

output = filter(lambda e:e.sal>10000 and e.age>21 and e.has_gf,list1)

for e in output:
    print(e.name)
    
    
# example 2:    
class employee:
    def __init__(self,name,sal,age,has_gf):
        self.name = name
        self.sal = sal
        self.age = age
        self.has_gf = has_gf
    def display(self):
        return self.name
e1 = employee('durga',20000,60,True)
e2 = employee('Ravi',4000,23,True)
e3 = employee('Shiva',2000,60,False)
e4 = employee('Pavan',5000,20,True)
e5 = employee('Kiran',50000,60,True)
e6 = employee('Teja', 60000, 22, True)

list1 = [e1,e2,e3,e4,e5,e6]

output = filter(lambda e:e.sal<10000 or e.sal>50000,list1)

for e in output:
    print(e.name)
    
# Example 3:

class employee:
    def __init__(self,name,sal,age,has_gf):
        self.name = name
        self.sal = sal
        self.age = age
        self.has_gf = has_gf
    def display(self):
        return self.name
e1 = employee('durga',20000,60,True)
e2 = employee('Ravi',4000,23,True)
e3 = employee('Shiva',2000,60,False)
e4 = employee('Pavan',5000,20,True)
e5 = employee('Kiran',50000,60,True)
e6 = employee('Teja', 60000, 22, True)

list1 = [e1,e2,e3,e4,e5,e6]

output = filter(lambda e:(e.sal>1000 and e.age>21 and e.has_gf) and not(e.sal<10000 or e.sal>60000),list1)

for e in output:
    print(e.name)
    
    
# map()function

def square(n):
    return n*n
list1 = [1,2,3,4,5]
output = list(map(lambda n:n*n,list1))
print(output)

def square(n):
    return n*n
list1 = [1,2,3,4,5]
output = list(map(lambda n:2*n,list1))
print(output)


class employee:
    def __init__(self,name,sal,age,has_hf):
        self.name = name
        self.sal = sal
        self.age = age
        self.has_hf = has_hf
    def display(self):
        return self.name
e1 = employee('Rajesh',60000,20, True)
e2 = employee('Shivam', 20000, 60, True)
e3 = employee('Arun', 50000, 60, False)
e4 = employee('Vimal', 6000, 60, True)
e5 = employee('Umesh', 80000, 30, False)
e6 = employee('Tarun', 45000, 40, True)


list1 = [e1,e2,e3,e4,e5,e6]
output = map(lambda e:employee(e.name,e.sal+10000,e.age,e.has_hf),list1)


for e in output:
    print(e.name,'....',e.sal)
    
    
# Student  Program:
    
    
class student:
    def __init__(self,name,clas,rollno,marks,gender):
        self.name = name
        self.clas = clas
        self.rollno = rollno
        self.marks = marks
        self.gender = gender
    def school(self):
        return self.name
e1 = student('Rajesh' ,6,1240, 68,'Male')
e2 = student('Varun' ,8,1150, 85,'Male')
e3 = student('Shivani' ,9,1085, 92,'Female')
e4 = student('Arun', 7,1190, 61,'Male')
e5 = student('Rohini' ,10,1321, 59,'Female')
e6 = student('mahesh' ,6,1110, 86,'Male')
e7 = student('Avani' ,7,1199, 73,'Female')
e8 = student('Umesh',9,1060, 51,'Male')
e9 = student('Balu' ,10,1005, 99,'Female')
e10 = student('Santhu',8,1113, 67,'Male')
e11 = student('Srikanth' ,7,1168, 54,'Male')
e12 = student('Ramya' ,6,1230, 65,'Female')
e13 = student('Kiran' ,10,1003, 72,'Female')
e14 = student('Yamini' ,9,1090, 49,'Female')
e15 = student('Prakash' ,7,1200, 54,'Male')
e16 = student('Sindhu' ,8,1112, 44,'Female')


list1 = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
output = filter(lambda e:e.clas>5 and e.rollno>1000  and e.marks>70 and e.gender>='Male',list1)
result = filter(lambda e:e.clas>5 and e.rollno>1000  and e.marks>90 and e.gender<='Female',list1)
print('This list only for boys:')
for e in output:  
    print(e.name)
print('This list only for Girls:')
for e in result:    
    print(e.name)
    












