# Explain nested if statemnts . provide a practical exam,such as checking if a number is positive and then checking if it is even.
num = 9
if num>0:
    print("number is positive")
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is negative")