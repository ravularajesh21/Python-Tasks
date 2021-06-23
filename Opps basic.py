## The __init__() Function


class employee:
    def __init__(self,name,salary,role,place):
        self.name = name
        self.salary = salary
        self.role = role
        self.place = place
        
job = employee('rajesh',600000,'python developer','hyderabad')

print(job.name)
print(job.salary)
print(job.role)
print(job.place)




# Object Method 

class employee:
    def __init__(self,name,age,experience,role):
        self.name = name
        self.age = age
        self.experience = experience
        self.role = role
        
    def office(self):
        print('Hello my name is'+self.name)
        print( +self.age)
        print(''+self.experience)
        print(''+self.role)
        
job=employee('rajesh', 26, 'nill','python web developer')
job.office()


# Self Parameter 

class myclass:
    def __init__(self,name,age,roll_no,subject,marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.subject = subject
        self.marks = marks
        
    def student(model):
    
        print('my name is '+model.name)
        print( +model.age)
        print( +model.roll_no)
        print('Subject is '+model.subject)
        print( +model.marks)

name=input('enter name:')
age = int(input('enter age:'))
roll_no=int(input('enter roll number:'))
subject=input('enter subject:')
marks=float(input('enter marks:'))       
output = myclass(name,age,roll_no,subject,marks)
output.student()

# Modify Object Properties

class myclass:
    def __init__(self,name,age,roll_no,subject,marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.subject = subject
        self.marks = marks
        
    def student(model):
    
        print('my name is '+model.name)
        print( +model.age)
        print( +model.roll_no)
        print('Subject is '+model.subject)
        print( +model.marks)

       
output = myclass('rajesh',25,13548,'science',85)
output.student()

output.name = 'chiru'
output.age = 65
output.roll_no = 13548
output.marks = 99
print(output.name)
print(output.age)
print(output.roll_no)
print(output.marks)







    
    
    
    
    
    
    
    
    
    
    
    
    





















