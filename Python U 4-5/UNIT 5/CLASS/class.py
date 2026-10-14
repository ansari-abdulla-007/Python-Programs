# what is a class?
# A class is a blueprint(desing).
# It defines:
#   Data(variables).
#   Functions(methods).
class student:
    name="Abdulla"
    age=18
# Topic 3:-> What is an object?
#object is an instance of a class.
# we can create many objects from one class.
s1=student()
print(s1.name)
# Topic 4:-> What is an instance(object)?
# Instance means real object created from class.
# Each instance has its own data.
s2=student()
s2.name="Ansari"
print(s2.name)