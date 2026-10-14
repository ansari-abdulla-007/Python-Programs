#Loop through the letters in the word.
for x in "Abduu":
    print(x)

#the range() function the loop through a set of a code a specified number of times we can use the range () function.
# the range function returns sequence of numbers from 0 by default and increments by 1 by default. and ends at a specified numbers.
# using the range function.
for y in range(10):
    print(y)

# the range function defaults to 0 as a starting value however it is possible to specified the starting valuse by adding a parameter:(range(2,6))
# which needs values from 2 to 6.(but not encluding 6)
for z in range(1,11):
    print(z)

# the range() function defaults to increment the sequence by one , however it is possible to specified the increment value by adding a third parameter.
#range(2,30,2) #first=start,second=last,third = increment.
for i in range(2,30,2):
    print(i)

#print each adjective for every.....
adj = ["Abduu","sahil","amit"]
fruits = ["mango","apple","banana"]
for x in adj:
    for y in fruits:
        print(x,y) 