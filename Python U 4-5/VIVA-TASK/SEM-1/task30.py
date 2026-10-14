# Write a Python program to demonstrate inheritance using:
# • A parent class Vehicle
# • A child class Car
# • Show how the child class accesses parent class methods.
class vehicle:
    def start(self):
        print("vehicle is starting")

class car(vehicle):
    def drive(self):
        print("car is driving")
my_car = car()
my_car.start()