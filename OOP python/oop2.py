class Student:
    def __init__(self):
        self.name = "Manzoor"
        self.age = 22
    def update(self):
        self.name = "Ali"
    def compare(self,other): # compare(who is calling,whom to compare)
        if self.age == other.age:
            return True
        else:
            return False
s1 = Student()
s2 = Student()
s2.name = "Mazhar"
s2.age = 18

s2.update()
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)

if s1.compare(s2):
    print("They are in same age")
else:
    print("They have different age")

class Demo:
    pass

demo = Demo()
print(id(demo))