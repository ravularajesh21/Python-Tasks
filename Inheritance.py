# Single Inheritance

class p:
    'Hello every one'
    def __init__(self,python,java,net,sql,oracle):
        self.python = python
        self.java = java
        self.net = net
        self.sql = sql
        self.oracle = oracle
    def choose1(self):
        print('The best course is',self.python)
        print('The choise course is',self.java)
class c(p):
    def choose2(self):
        print('The avg course is',self.oracle)
m=c('1st','2nd','3rd','4th','5th')
m.choose2()
m.choose1()

# Multilevel Inheritance

class P:
    'Hello every one'
    def __init__(self,python,java,net,sql,oracle):
        self.python = python
        self.java = java
        self.net = net
        self.sql = sql
        self.oracle = oracle
    def choose1(self):
        print('The best course is',self.python)
        print('The choise course is',self.java)
class C(P):
    def choose2(self):
        print('The avg course is',self.sql)
class D(C):
    def choose3(self):
        print('The best course is',self.python)
        print('The normal course is',self.oracle)
m=D('1st','2nd','3rd','4th','5th')
m.choose3()
m.choose2()


# Hierarchical Inheritance

class P:
    'Hello every one'
    def __init__(self,python,java,net,sql,oracle):
        self.python = python
        self.java = java
        self.net = net
        self.sql = sql
        self.oracle = oracle
    def choose1(self):
        print('The best course is',self.python)
        print('The choise course is',self.java)
class C(P):
    def choose2(self):
        print('The avg course is',self.sql)
class D(P):
    def choose3(self):
        print('The best course is',self.python)
        print('The normal course is',self.oracle)
m=C('1st','2nd','3rd','4th','5th')
m.choose2()
m.choose1()




















