# Q18.
# Write a Python program to:
# • Create a list of numbers [1, 2, 3, 4, 5]
# • Use a lambda function with map() to double each element
# • Display the updated list.
nums = [1,2,3,4,5]
# using map() to apply a lambda function to each number in nums.
# lambda x: x*2 --> multiplies each element by 2.
# map() returns a map object, so we convert it to list.
squares = list(map(lambda x: x * 2,nums)) 
print(squares)