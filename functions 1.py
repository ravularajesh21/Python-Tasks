# Functions

def calculation(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    
calculation(10,25)

#There are two types of functions
# 1.Build in functions
# 2.User defined functions

#Print wish message
def wish(name):
    print('Hello {},Good morning'.format(name))
wish('Rajesh')

# print square value
def square(num):
    print('The square of {} is  {}'.format(num,num**2))
square(5)


#Types of arguments/parameters
#1.positional arguments
#2.Keyword arguments 
#3.Default arguments
#4.Variable lengh arguments

# Keyword arguments

def sub(a,b):
    print(a-b)
sub(10,b=20)

# Default arguments

def wish(name = 'Guest'):
    print('Hello',name,'Good morning')
wish()

def wish(name = 'Guest'):
    print('Hello',name,'Good morning')
wish('Rajesh')

# Varial lengh arguments

def sum(*n):
    print(n)
sum(10,20,30)

def sum(n,*s):
    print(n)
    print(s)
sum(10,20,30,40)


# Types of Variables
# 1.Global variable
# 2.Local variable

# Global variable:
    
a = 10
def f1():
    print(a)
def f2():
    print(a)
f1()
f2()

# Local variable:
    
def f1():
    a = 10
    print(a)
def f2():
    print(a)
f1()
f2()


# Global Keyword

a = 10
def f1():
    a = 888
    print(a)
def f2():
    print(a)
f1()
f2()

a = 10
def f1():
    global a
    a = 888
    print(a)
def f2():
    print(a)
f1()
f2()


def f1():
    global a
    a = 888
    print(a)
def f2():
    print(a)
f1()
f2()


a = 10
def f1():
    global a
    a = 888
    print(a)
def f2():
    a = 999
    print(a)
f1()
f2()
print(a)


a = 10
def f1():
    global a
    a = 888
    print(a)
def f2():
    global a
    a = 999
    print(a)
f1()
f2()
print(a)


# Factorial:
    
5! = 5*4*3*2*1
4! = 4*3*2*1

5! = 5*4!
5! = 5(5-1)!
n = n*(n-1)!
    
        
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = int(input('enter number:'))
output = fact(n)
print('factorial of',n,'is',output)


# Completion of finding factorial:
      
def fact(n):
    if n == 0:
        return 1
    else:
        result = n*fact(n-1)
    print('factorial of {} and result is {}'.format(n,result))
    return result
n = int(input('enter number:'))
out = fact(n)



# Fibonacci series:
    
    
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n = int(input('enter number:'))
out = fib(n)
print('fibonaci value of',n,'is',out)










    




