# 1. Access Name Mike
# 2. Access the value 88 or marks scored in math
# 3. change the name mike to yor name
# 4. Add Science = 80, English = 93

dict1={
       'my_batch':{
           'Student':{
               'Name':'Mike',
               'marks':{
                   'Python':95,
                   'Math':88,
                   'full stack':90
                   }
               }
           }
       }

print(dict1['my_batch']['Student']['Name'])
print(dict1['my_batch']['Student']['marks']['Python'])
dict1['my_batch']['Student']['marks']['Python']=55
dict1['my_batch']['Student']['Name']='Rajesh'
dict1['my_batch']['Student']['marks']['English']=99
dict1['my_batch']['Student']['marks']['Science']=75
print(dict1)
print(dict1['my_batch']['Student']['Name'])
print(dict1['my_batch']['Student']['marks']['Python'])
print(dict1['my_batch']['Student']['marks']['Math'])
print(dict1['my_batch']['Student']['marks']['full stack'])
print(dict1['my_batch']['Student']['marks']['English'])
print(dict1['my_batch']['Student']['marks']['Science'])



