'''
class car():
    pass
ford = car()
honda = car()
audi = car()

ford.speed = 200
honda.speed = 100
audi.speed = 150

ford.color = 'red'
honda.color = 'blue'
audi.color = 'black'

print(ford.speed)
print(ford.color)

ford.speed = 20000
ford.color = 'redddddddd'

print(ford.speed)
print(ford.color)

class rectangle:
    pass
rec1 = rectangle()
rec2 = rectangle()

rec1.height = 10
rec2.height = 20

rec1.width = 50
rec2.width = 40

a = (rec1.height * rec1.width)
b = (rec2.height * rec2.width)
print("Ans=",a,",", b)

class car():
    def __init__(self, speed, color): # (self) is as you like, give name 
        print(speed)
        print(color)
        self.speed = speed #line no-60
        self.color = color #line no-61
        print("the__init__is called")

ford = car(200, 'red')
honda = car(300, 'blue')
audi = car(100, 'black')

# ford.speed = 200
# honda.speed = 100
# audi.speed = 150

# ford.color = 'red'
# honda.color = 'blue'
# audi.color = 'black'

print(ford.speed)
print(ford.color)

class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

rec1 = rectangle(20, 20)
rec2 = rectangle(30, 30)

# rec1.height = 10
# rec2.height = 20
# rec1.width = 50
# rec2.width = 40

print(rec1.height * rec1.width)
print(rec2.height * rec2.width)

class car():
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    
    def set_speed(self, value):
        self.speed = value

    def get_speed(self):
        return self.speed

ford = car(100, 'red')
honda = car(200, 'blue')
audi = car(300, 'black')

ford.set_speed(300)
ford.speed = 400
print(ford.get_speed())
print(ford.color)

class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30
hello = Hello('name')
print(hello.a)
print(hello._b)
print(hello.__c)

class car():
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color
    
    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = car(100, 'red')
honda = car(200, 'blue')
audi = car(300, 'black')

ford.set_speed(300)
print(ford.get_speed())
print(ford.get_color())

class rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def set_height(self, height):
        self.__height = height
    def get_height(self):
        return self.__height
        
    def set_width(self, width):
        self.__width = width
    def get_width(self):
        return self.__width
        
    def area(self):
        return self.__height * self.__width

rec1 = rectangle(20, 20)
rec2 = rectangle(30, 30)

print(rec1.area())
print(rec2.area())

class polygon:
    #__width = None
    #__height = None 

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height

class Rectangle(polygon):
    def area(self):
        return self.get_width() * self.get_height()

class Triangle(polygon):
    def area(self):
        return self.get_width() * self.get_height() / 2

rect = Rectangle()
tri = Triangle()

rect.set_values(50, 40)
tri.set_values(20, 30)
print(rect.area())
print(tri.area())

class Salary:
    pay=0
    bonus=0
    def __init__(self): 
        self.pay = int(input("Enter pay = "))
        self.bonus = int(input("Enter bonus = "))
        # self.pay = pay
        # self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    name =""
    age=0
    obj_salary=0
    def __init__(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        # self.name = name
        # self.age = age
        self.obj_salary=Salary()
    
    def total_salary(self):
        return self.obj_salary.annual_salary()

emp = Employee()
# print("Emp name =", emp.name)
print("Total emp = ",emp.total_salary())

class Employee:

    def __init__(self):
        self.name=""
        self.age=0
        self.pay=0
        self.bouns=0
    
    def register(self):
        self.name=input("Enter name : ")
        self.age=int(input("Enter age : "))
        self.pay=int(input("Enter pay : "))
        self.bouns=int(input("Enter bouns : "))
    
    def totalsalary(self):
        return (self.pay * 12) + self.bouns

if __name__=="__main__":
    emp1 = Employee()
    emp1.register()
    print("Total salary = ",emp1.totalsalary())

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return 4 * self.__side

square = Square(5)
print(square.area())
print(square.perimeter())

class CoffeeCup:
    def __init__(self, temperature):
        temperature = int(input("Enter Coffee Temperature : "))
        self.temperature = temperature
    def drink_coffee(self):
        if self.temperature > 85:
            print('Coffee Too Hot')
        elif self.temperature < 65:
            print('Coffee Too Cold')
        else:
            print('Coffee Ok to Drink')

if __name__=="__main__":
    cup = CoffeeCup(0)
    cup.drink_coffee()
class CoffeeCup:
    def __init__(self, temperature):
        self.temperature = temperature
    def drink_coffee(self):
        if self.temperature > 85:
            print('Coffee Too Hot')
        elif self.temperature < 65:
            print('Coffee Too Cold')
        else:
            print('Coffee Ok to Drink')

cup = CoffeeCup(100)
cup.drink_coffee()
  

# ----*****    Programming 72 Coder   ******-----

# hello we going to explore OOP in Python
class waifer:
    name = 'Waifer'
    age = 28
    def method1 (self):
        return "hey i am method one"    # return = print
    def method2 (self):
        return "hey i am method two"
    def method3 (self,x):
        self.name = x
        #return x
kolar = waifer()
print (kolar.name)
print (kolar.age)
print (kolar.method1())
print (kolar.method2())
print (kolar.method3('what is waifer'))
print (kolar.name)
'''
class goofy:
    def one(self,name):
        self.name=name
    def two(self):
        return self.name
    def three(self):
        return "Hello %s" % self.name
c=goofy()
d=goofy()

c.one("waifer")
d.one("kolar")
print (c.two())
print (d.two())
print (c.three())
print (d.three())