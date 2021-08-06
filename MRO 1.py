# Exm 1 :
   
class A:
    def process(self):
        print('AAa** processed')
class B:
    def process(self):
        print('B processed')
class C(A,B):
    def process(self):
        print('C processed')
class D(C,B):
    pass

my = D()
my.process()


# Exm 2 :

class A:
    def process(self):
        print('Hello')
class B:
    def process(self):
        print('Hi')
class C(A,B):
    pass
class D(C,B):
    pass
my = D()
my.process()    

# Exm 3:

class A:
    def process (self):
        print('welcome to my home')
class B:
    def process(self):
        pass
class C(A,B):
    pass
class D(C,B):
    pass
my = D()
my.process()

# Exm 4:
    
class A:
    def process(self):
        print('Hello')
class B(A):
    pass
class C(A):
    def process(self):
        print('Welcome to my website')
class D(B,C):
    pass
my = D()
my.process()

# Exm 5:
    
class A:
    def villa(self):
        print('Hello')
class B(A):
    def villa(self):
        print('Hi')
class C(A,B):
    pass

my = C()
my.villa()
        
# Exm 6:
    
class A:
    def __init__(self):
        print('A')
class B:
    def __init__(self):
        print('B')
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

my = C()
my.__init__()









