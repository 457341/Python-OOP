class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
       print("Config is: ",self.cpu,self.ram)

# comp1 = Computer()
# comp2 = Computer()
# Computer.config(comp1) # not commonly used
# Computer.config(comp2)
# Commonly used

comp1 = Computer("i5","8GB")
comp2 = Computer("Ryzen 3","16GB")
comp1.config()
comp2.config()


class Student:
    def __init__(self):
        print("This is simple class")
    def __init__(self,name): # it tried it like in Java programming but not working
        self.name = name
        print("My name is: ",self.name)

student1 = Student("Hussain")
student2 = Student("Manzoor")
