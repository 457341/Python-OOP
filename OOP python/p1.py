name = "manzoor"
surname = "hussain"
fullName = name.capitalize() + " "+surname.upper() +  " " +"mughal".capitalize()
print("My name is: ",fullName)

# lists
# A list stores a series of items in a particular order. You access items 
# using an index, or within a loop\
countries = ["Pakistan","Turkey","India","USA"]
print(countries[:]) #prints all elements
print(countries[0])#prints first element
print(countries[-1])#prints last element
countries.append("Canada")
countries.append("Germany")
for i in countries:
    index = countries.index(i) # To trace the indeces
    print("Element ",index ,"is: ",i)
    #print("Element")
    #print(countries[i])

#initializing new blank list
names = []
names.append("Manzoor")
print(names[:])
print("\n")
names.extend(["Ali","Ahmed","Khalid","Tauheed"]) #Adding multiple values to a list
print(names[:],"\n")
print(names[:2],"\n")
print(names[1:3]) #printing elements from index 1 to 2(index 3 in not included)

empty_list = []
mixed_list = ["manzoor",22,3.14]
nexted_list = ["Manzoor",[1,2],["Hussain",3,8.9]]


new_list = [2**i for i in  range(11)] # making list excluding last digit(here 11)
print(new_list)

def manzo():
    #print("manzoor")
    return "Manzoor"

print("Wow it is working: ",manzo())


def BubbleSort():
    return 
print(BubbleSort())