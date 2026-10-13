#Write a Python program using a nested if statement to find the largest of three numbers.
x = 50 
y = 60 
z = 77
if x>y:
    if x>z:
        print("x is the largest number!")
else:
    if y>z:
        print("y is the largest number!")
    else:
        print("z is the largest number!")