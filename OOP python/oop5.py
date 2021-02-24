# Inner classes
class Student:
    def __init__(self,name,roll_No):
        self.name = name
        self.roll_No = roll_No
        self.lap = self.Laptop()
    def show(self):
        print(self.name,self.roll_No)
        self.lap.show() # We can also call from here

    # Inner class
    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8GB"
        def show(self):
            print("Config is: ",self.brand,self.cpu,self.ram)


student1 = Student("Manzoor",755)
student2 = Student("Mushtaq",759)
student1.show()
student2.show()
print(student1.lap.brand)
lap1 = student1.lap # object
lap2  = student2.lap #object
print(lap1)
student3 = Student.Laptop()
student3.show()