# Decorator

# Without link between decorator and function

def decor(func):
    def inner():
        print('Hello Python')
        print('Hello Rajesh')
    return inner
def vision():
    print('Showing a person')
vision()

# Link between decorator and function

def decor(func):
    def inner():
        print('Hello Python')
        print('Hello Rajesh')
    return inner

@decor
def vision():
    print('Showing a person')
vision()

# Exm 1:
    
def decor_for_add(func):
    def inner(x,y):
        print('#'*10)
        print('The sum of {} and {} is : '.format(x,y),end=(""))
        func(x,y)
        print('#'*10)
    return inner

@decor_for_add
def add(a,b):
    print(a+b)
add(10,20)

# Exm 2 :

def decor_for_Rajesh(func):
    def inner(name):
        if name == 'Rajesh':
            print('#'*10)
            print('Hello Rajesh your very impartant for us')
            print('Very Very Good Morning')
            print('#'*10)
        else:
            func(name)
    return inner

@decor_for_Rajesh
def hello(name):
    print('Good Morning:',name)
hello('Rajesh')

# Exm 3 :

def decor_for_Rajesh(func):
    def inner(name):
        if name == 'Rajesh':
            print('#'*10)
            print('Hello Rajesh your very impartant for us')
            print('Very Very Good Morning')
            print('#'*10)
        else:
            func(name)
    return inner

@decor_for_Rajesh
def hello(name):
    print('Good Morning:',name)
hello('Ganesh')

# Exm 4 :
    
def decor_for_Rajesh(func):
    def inner(name):
        names = ['CM','PM','Minister','President']
        if name in names:
            print('#'*10)
            print('Hello {},you are very impartant for us'.format(name))
            print('#'*10)
        else:
            func(name)
    return inner

@decor_for_Rajesh
def view(name):
    print('Hello every one:',name)
view('CM')

# Exm 5 :
    
def decor_for_Rajesh(func):
    def inner(name):
        names = ['CM','PM','Minister','President']
        if name in names:
            print('#'*10)
            print('Hello {},you are very impartant for us'.format(name))
            print('#'*10)
        else:
            func(name)
    return inner

@decor_for_Rajesh
def view(name):
    print('Hello every one:',name)
view('Arun')

# Division with zero without getting any error

# Exm 1:
def smart_division(func):
    def inner(a,b):
        if b == 0:
            print('Hello stupid,how we can divide with zero')
        else:
            func(a,b)
    return inner

@smart_division
def division(a,b):
    print(a/b)
division(10,2)

# Exm 2:
    
def smart_division(func):
    def inner(a,b):
        if b == 0:
            print('Hello stupid,how we can divide with zero')
        else:
            func(a,b)
    return inner

@smart_division
def division(a,b):
    print(a/b)
division(10,0)