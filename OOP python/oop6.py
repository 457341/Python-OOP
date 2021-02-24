# Here we talked about 3 things
# 1. Single level inheritance
# 2.  Multilevel inheritance
# 3. Multiple inheritance

class A:
    def feature1(self):
        print("Providing feature1")
    
    def feature2(self):
        print("Providing featur2")


class B(A): #single level inheritance
    def feature3(self):
        print("Providing feature3")


class C(B): # multilevel inheritance
     def feature4(self):
        print("Providing feature4")


class D:
     def feature5(self):
        print("Providing feature5")


class E(A,D): # Multiple inheritance
     def featur6(self):
        print("Providing feature6")