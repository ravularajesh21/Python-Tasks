# Multi Level Inheritance:

# Exm 1 :
    
class College:
    def __init__(self,staff,furniture,clas_room,students,lab):
        self.staff = staff
        self.furniture = furniture
        self.clas_room = clas_room
        self.students = students
        self.lab = lab
    def Study(self):
        print('Im one of the staff in this clg',self.staff)
        print('Equepment is',self.furniture)
class School(College):
    def Tree(self):
        print('Class rooms are',self.clas_room)
        print('Students are',self.students)
class Primary(School):
    def Yah(self):
        print('Lab is',self.lab)

my = Primary('Rajesh','Benches,chairs,Tables',20,1500,'Computer lab')
my.Yah()
my.Study()
my.Tree()

# Exm 2 :
    
class College:
    def __init__(self,staff,furniture):
        self.staff = staff
        self.furniture = furniture
        
    def Study(self):
        print('Im one of the staff in this clg',self.staff)
        print('Equepment is',self.furniture)
class School(College):
    def __init__(self, staff, furniture,clas_room,students):
        super().__init__(staff, furniture)
        self.clas_room = clas_room
        self.students = students
        
    def Tree(self):
        print('Class rooms are',self.clas_room)
        print('Students are',self.students)
class Primary(School):
    def __init__(self, staff, furniture, clas_room, students,lab):
        super().__init__(staff, furniture, clas_room, students)
        self.lab = lab
    def Yah(self):
        print('Lab is',self.lab)

my = Primary('Rajesh','Benches,chairs,Tables',20,1500,'Computer lab')
my.Yah()
my.Tree()
my.Study()

# Exm 3 :
    
class A:
    x,y = 10,20
    def m1(self):
        a,b = 15,25
        print(a+b)
        print(self.x+self.y)
class B(A):
    c,d = 100,200
    def m2(self):
        e,f = 35,45
        print(e+f)
        print(self.c+self.d)
class C(B):
    i,j = 1,2
    def m3(self): 
        k,l = 3,5
        print(k+l)
        print(self.i+self.j)
hi = C()
hi.m1()
hi.m2()
hi.m3()

# Exm 4 :
    
x,z = 1000,2000
class A:
    x,y = 10,20
    def m1(self):
        a,b = 15,25
        print(a+b)
        print(self.x+self.y)
class B(A):
    c,d = 100,200
    def m2(self):
        e,f = 35,45
        print(e+f)
        print(self.c+self.d)
        print(globals()['x']+globals()['z'])
        print(super().x+super().y)   # immediate parent
        print(A().x+A().y)           # First parent
class C(B):
    i,j = 1,2
    def m3(self): 
        k,l = 3,5
        print(k+l)
        print(self.i+self.j)
hi = C()
hi.m1()
hi.m2()
hi.m3()


