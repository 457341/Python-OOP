# Operator Overloading
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1 
        self.m2 = m2

    def __str__(self):
        # return self.m1, self.m2 # it will return tuple
        return '{} {}'.format(self.m1,self.m2) # Avoiding returning tuple

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, value):
        v1 = self.m1 + self.m2
        v2 = value.m1 + value.m2
        if v1 > v2:
            return True
        else:
            return False

s1 = Student(2,3)
s2 = Student(5,15)
s3 = s1 + s2 # Student.add(s1,s2)
print(s3.m1)
print(s3.m2)
if s1 > s2:
    print("S1 Wins")
else:
    print("S2 Wins")

a = 9
print(a)
# print(a.__str__()) # Returns same as upper line
# print(s1)
# print(s1.__str__()) # Returns same as upper line
# if we want to return only values, We can change it by overriding __str__() method
print(s1)
print(s1.__str__())