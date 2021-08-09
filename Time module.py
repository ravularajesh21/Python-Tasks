import time

a= time.time()
print(a)

b= time.ctime(1628525422.7894645 )
print(b)

c= time.localtime()
print(c)

a= time.localtime()
b = time.mktime(a)
print(b)

c = time.asctime(a)
print(c)

x = time.strftime('%m/%d/%Y')
print(x)

y = '09 August 2021'
s = time.strptime(y,"%d %B %Y")
print(s)

# Datetime :
    
import datetime

a = datetime.datetime(2021, 8, 9,10,30,55,458)
print(a)

b = datetime.datetime.today()
print(b)

c = datetime.datetime.now()
print(c)

u = c.year
print(u)

m = c.month
print(m)

i = c.date()
print(i) 

print(c.hour)
print(c.month)

b1 = datetime.timedelta(days = 20)
b2 = datetime.timedelta(days = 30)
b3 = b1-b2
print(b3)








