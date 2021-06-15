##Dictionary Data Type

dict1={1:10,2:20,3:30,4:40,5:50}
print(dict1)
print(type(dict1))

# duplicates keys are not allowed but values can be dublicated:

dict2={1:10,2:20,1:15,3:30,2:85,4:50,5:55,4:35,1:65,2:25,5:100,3:45,4:23}
print(dict2)
dict3={'rajesh':45000,'manasa':65000,'arun':68000,'shivam':50000}
print(dict3)
dict3['rajesh']=60000
print(dict3)

#Convert from other types to dict:
#Convert from list type to dict:
list1=[(1,10),(2,20),(3,30),(4,40),(5,50)]
dict4=dict(list1)
print(dict4)
#Convert from tuple  type to dict:
tuple1=((1,'rajesh'),(2,'arun'),(3,'shivam'),(4,'suresh'),(5,'venkatesh'))
dict5=dict(tuple1)

#Convert from set type to dict:
set1={(2,1.555),(3,35),(4,True),(5.5,2.333),(True,'rajesh'),('manasa',10+25j)}
dict6=dict(set1)
print(dict6)

#add two list and convet to dict
l1=[1,2,3,4,5]
l2=[15,25,35,45,55]
z=zip(l1,l2)
dict7=dict(z)
print(dict7)

# accessing elements using keys:
score={'rohit':85,'virot':45,'dhoni':65,'tarun':35,'umesh':15,'dhawan':112}
print(score['dhawan'])
#print(score['rajesh'])  # To get key error (key is not exists in dict)

# accessing elements using keys whithout  any error (Using .get())
score={'rohit':85,'virot':45,'dhoni':65,'tarun':35,'umesh':15,'dhawan':112}
print(score['dhoni'])
print(score.get('arun'))
print(score.get('mahesh babu'))

#Dictionary view objects:
    # 1.Keys()  2.Values()  3.items()
# Keys()
phone_dict={'naresh':9845862471,'suresh':7995421564,'kishore':8945766542,'arun':9547684213}
names=phone_dict.keys()
print(names)
names_list=list(names)
print(names_list)
for name in names_list:
    print(name)
    
# Values() 
numbers=phone_dict.values()
dict1=list(numbers)
print(dict1)
for number in dict1:
    print(number) 
    
# Items()  
data=phone_dict.items()
print(data)
for names,numbers in data:
    print(names,numbers)
    
# Adding item inside dictionary
#1.Add()  2.Update()
# Add()
num={1:10,2:20,3:30,4:40,5:50,6:60}
num[7]=70
num[1]=True
num[2]=24.5
num[4]='Python'
print(num)

# Update()
num={1:10,2:20,3:30,4:40,5:50,6:60}
num2={1.5:15,2.5:25,3.5:35,4.5:45}
num.update(num2)
print(num)    
 
# How to remove content of dictionary
# 1.del() 2.clear() 3.pop() 
# del()
dict1={1:True,2:'naresh',3:30+25j,4:4.5,5:'mahesh',6:60}
del dict1[3]
del dict1[6]    #if key is not exists it raises key error
print(dict1)

# Clear()
dict1={1:True,2:'naresh',3:30+25j,4:4.5,5:'mahesh',6:60}
dict1.clear()
print(dict1)

# Pop()
dict1={1:True,2:'naresh',3:30+25j,4:4.5,5:'mahesh',6:60}
data=dict1.pop(2)
data=dict1.pop(20,None)
print(data)
print(dict1)

# setdefault()
d={1:10,2:20,3:30,4:40,5:50}
print(d.setdefault(1,True))   #output is 10
print(d.setdefault(10,True))

# Nested dictionary
dict1={
       '1st person':{'name':'rajesh',
                     'year':1996,
                     'profession':['python web developer',]},
         '2nd person':{'name':'ramesh',
                     'year':1995,
                     'profession':['java web developer']}}
print(dict1['1st person'])
print(dict1['2nd person'])
print(dict1['1st person']['name'])
print(dict1['1st person']['year'])
print(dict1['1st person']['profession'])
















