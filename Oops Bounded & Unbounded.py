# Unbounded

# Exm 1:
    
class Hotel:
    def Menu(food,cost,location,Rooms):
        print(food,cost,location)
    def Tasty(location,Rooms):
        print(location,Rooms)
    def Price(food,Rooms):
        print(food,Rooms)
    
    

Hotel.Menu('Biryani','500','Hyderabad','50')
Hotel.Tasty('Hyderabad','50')
Hotel.Price('Biryani','50')


# Exm 2:
    
class School:
    def Class1(students,staff,workers):
        print(students)
    def Class2(staff):
        print(staff)
    def Class3(workers):
        print(workers)

School.Class1('Rajesh','Teacher','Sleeper')
School.Class2('Teacher')
School.Class3('Sleeper')

# Bounded

# Exm 1:
    
class Mfg:
    def __init__(self,bikes,cars,airoplane):
        self.bikes = bikes
        self.cars = cars
        self.airoplane = airoplane
    def Sales(self):
        print('The Trending Bike is',self.bikes)
        print('The Latest car is',self.cars)
    def Cost(self):
        print('The price of the airoplane is',self.airoplane)
        
my = Mfg('Pulsar','oodi','800cr')
my.Sales()
my.Cost()

# Exm 2:

class Shop:
    def __init__(self,things,service,cash,space):
        self.things = things
        self.service = service
        self.cash = cash
        self.space = space
    def Small(self):
        print('Products is',self.things)
        print('The best services is',self.service)
    def Big(self):
        print('Best low chargers',self.cash)
    def Middle(self):
        print('Best space is',self.space)

my = Shop('Boost','delivery',50,'Warangal')
my.Small()
my.Middle()
my.Big()
        
        











