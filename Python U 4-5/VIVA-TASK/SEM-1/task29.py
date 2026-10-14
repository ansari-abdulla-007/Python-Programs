# Write a Python program to:
# • Create a class with a destructor
# • Display a message when the object is destroyed.
class demo:
    def __del__(self):
        print("Object destroyed")