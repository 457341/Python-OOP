#Method Types
#1.Class methods: works for class variables
#2.Instance methods: works for instance variables
#3.static methods: Nothing to do with variables, we want something ectra

class Student:
    school = "Omu"
    def __init__(self,mark1,mark2,mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
# Instance method
# There are two types of instance methods: 1.Accessors(getters), 2.Mutator(setters)

    def average(self):
        return (self.mark1 + self.mark2 + self.mark3)/3

# Getter method
    def get_mark1(self):
        return self.mark1
# Setter Method
    def set_mark1(self,value):
        self.mark1 = value
# To be able to work with class variables we use class methods
    @classmethod 
    # class getter method
    def get_school(cls):
        return Student.school
    # class setter method
    @classmethod 
    def set_school(cls,value): # class setter(mutator: means changer) methods
        Student.school = value
    
    @staticmethod # Static method
    def info():
        print("Hey! This is my class")
s1 = Student(70,30,90)
s2 = Student(55,66,81)
print("Student 1 Average: ",s1.average())
print("Student 2 Average: ",s2.average())
print("My School name is: ",Student.school)
print("My school name is: ",Student.get_school()) # with the help of class getter method
Student.set_school("Mit")
print("My school name is: ",Student.get_school()) # with the help of class getter method
Student.info()
