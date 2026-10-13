# Write a Python program to:
# • Create a class Student
# • Define a constructor that accepts name and age
# • Create an object using the constructor
# • Display the student details.
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1=student("Abdulla",18)
print(s1.name)
print(s1.age)