# WAP to find the factorial of first n numbers.(using for)
n = 5
factorial = 1

for i in range(1, n+1):
    factorial*=i

print("factorial =", factorial)