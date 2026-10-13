#programming demonstrating while loop,if-elif-else, and logicsl operator.
num=1
while num<=5:
    if num>0 and num%2==0:
        print(num,"is positive and even")
    elif num>0 and num%2!=0:
        print(num,"is positive and odd")
    else:
        print(num,"is not positive")
    num+=1