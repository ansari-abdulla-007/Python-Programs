# Write a Python program to:
# • Create a class with a constructor
# • Create two objects with different values
# • Print the data of both objects.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("Ansari",18)
s2=student("Sahil",19)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)