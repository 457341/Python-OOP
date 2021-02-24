# Here we talked about 3 things
# 1.How constructor behaves in inheritance
# 2. How to use super() in inheritance
# 3. Method Resolution Order(MRO): from left to right

class A:
    def __init__(self):
        print("In class A")
    def fun1(self):
        print("Funtion 1")

    def foo(self):
        print("class A foo()")

class B(A):
    def __init__(self):
        super().__init__()
        print("In class B")
    def fun2(self):
        print("Funtion 2")
a1 = B()

class D:
    def foo(self):
        print("class D foo()")

class E(A,D):
    def baz(self):
        return 0

b = E()
b.foo() # Will call foo() from class A not from Class D, because it works from left to right.
