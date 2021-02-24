# Method Overriding
# What is Method overriding? 
# In heritance if we have method with same name, same no of parameters, same data types of parameters
class A:
    def show(self):
        print("In class A")

class B(A):
    def show(self): # This is method overriding because B class has already show() method (in class A because of inheritance)
        print("In class B")
    
a = B()
a.show()
