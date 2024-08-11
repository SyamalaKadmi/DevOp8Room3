#Lists - ordered

# allClassStudent = ["Rahul", "Rohan"]

# allClassStudent.append("Rehan")

# for i in range(len(allClassStudent)):
#     print(allClassStudent[i])

# allClassStudent.remove("Rohan")

# for i in allClassStudent:
#     print(i)


# Write a python program which asks if you want to add  a name, 
# if you reply yes then it asks you to write the name, which you will add in a list. 
# If it is no, then you display all the names which was added.
#  While, if/else, list, input(), print()

# value = input("Please type 'yes' to add names and 'no' to exit: ")
# names = []
# while (value == 'yes'):
#     name = input("Please enter the name: ")
#     names.append(name)
#     value = input("Please type 'yes' to add names and 'no' to exit: ")

# print(names)


#Sets - unordered, doesn’t store duplicate values, can be changed (mutable)
allStudent = {'apple','mango', 1, 2, 3, 4}
allStudent.add('pineapple')
allStudent.remove('apple')
print(allStudent)

#Tuples - very similar to list, but it is immutable
flowerTuple = ('rose', 'lily','sunflower', 'tulip')
print(flowerTuple)

#Dictionary - key, value pairs
instance = {
    "name": "DXQWL",
    "OS": "MacOS",
    "make": 2020
}

for i in instance:
    print(i)
    print(instance[i])

print(instance)

classStudents = [
    {
        "name": "DXQWL",
        "OS": "MacOS",
        "make": 2020
    },
    {
        "name": "WFDL",
        "OS": "MacOS",
        "make": 2020
    }
]

print(classStudents[1]['name'])