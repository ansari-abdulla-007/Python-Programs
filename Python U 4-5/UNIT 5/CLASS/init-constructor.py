# Constructor is a special method.
# It runs automatically when object is created.
# Constructor name: __init__()

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
# object with constructor:-
s1=student("Ansari",18)
print(s1.name)
print(s1.age)

# Destructor in python:-
# Destructor is used to destroy object.
# Method name: __del__()
# Called automatically.
class demo:
    def __del__(self):
        print("Object destroyed")