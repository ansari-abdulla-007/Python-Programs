# What is inheritance?
# inheritance means one class uses another class prperties.
# child class gets methods and variables of parent class.
# this helps code reuse.

class animal:
    def speak(self):
        print("Animal speaks")
#explanation:-Animal is a parent class.
            #: speak() is a method of animal.
class dog(animal):
    def bark(self):
        print("Dog barks")
#Explanation:-dog is a child class.
        #dog(animal) means dog inherits animal.
        #dog can use:
            #speak()(from animal)
            #bark()(its own method)
d=dog()
d.speak()
d.bark()

# dogs class automatically gets animal class methods.