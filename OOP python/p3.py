
name = input("Enter your name: ")
print("My name is: ",name)
print("The length of my name is: ",len(name))
ages = [5,13,17,18,24,32]
def myFunc(x):
    if x <18:
        return False
    else:
        return True

adults = filter(myFunc,ages)
for x in adults:
    print (x,end =" ") # if you want to print in same line
    # print (x,end =", ")
    # print (x,end =",, ")
