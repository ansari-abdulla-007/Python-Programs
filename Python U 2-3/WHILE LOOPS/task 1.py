# start by setting i to 1.
i = 1
#run the loop i is lessthen 6.
while i <= 6:
    print(i)
    i+=1

# with the  break statement  we can stop the loop even if the while condition is truee.
# exit the loop when i is 3.
i = 1
while i<6:
    print(i)   
    if i == 3:
        break
    i +=1

# with the continue statement we can stop the current ittaration and continue with the next.
# continue to the ittaration if i is 3.
i = 0
while i <6:
    i += 1
    if i == 3:
        continue
    print(i)