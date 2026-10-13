# Write a Python program to:
# • Accept a number from the user
# • Check:
# o If the number is positive
# ▪ Check whether it is even or odd
# o Else print that the number is negative or zero.
num = int(input("Enter a number:"))
if num >0:
    print("The number is positive")
    if num%2==0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Number is negative")