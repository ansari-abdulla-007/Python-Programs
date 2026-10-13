# Write a Python program that:
#  Uses a lambda function
#  Applies it with map() to double the elements of a list
#  Displays the final output.

nums = [1,2,3,4]
# using map() to apply a lambda function to each number in nums.
# lambda x: x*2 --> multiplies each element by 2.
# map() returns a map object, so we convert it to list.
squares = list(map(lambda x: x * 2,nums)) 
print(squares)