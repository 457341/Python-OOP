# Method Overloading
# What is Overloading: In same class same method name but different data types of parameters or no of parameters
# In python it is not supported directly but we can do by an alternative way.


class Foo:
    def sum(self,a = None,b =None,c = None):
        s = 0
        if a!= None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b 
        elif a != None:
            s = a
        else:
            s = 0
        return s

f = Foo()
print(f.sum(1,2,3))
print(f.sum(1,2))
print(f.sum(1))
print(f.sum())