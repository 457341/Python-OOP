# Variable Types in Python
# 1. instance variable : Every object has different instance variable value
# 2. class variable(static variable) : All objects share same value, if it changes it will effect all other objects

class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10 # instance variable
        self.company = "BMW" # instance variable
    
car1 = Car()
car2 = Car()
print(car1.mil, car1.company,car1.wheels)
print(car2.mil, car2.company,car2.wheels)
car1.mil = 9 # will not effect to the value of car2 object
Car.wheels = 5 # will change for all class
car1.wheels = 6 # will change only for car1
print(car1.mil, car1.company,car1.wheels)
print(car2.mil, car2.company,car2.wheels)

print(Car.wheels) # We can also print in this form