#1. what is lambda function.
# A lambda function is a small anonymous function in pyhton.
# it can take any number of arguments but has only one expression.
# lambda functions are useful when you you need a simple function for a short task.
# Syntax -> lambda arguments: expression

#2. why use lambda functions?
# they are shorter and faster to write than normal functions.
# useful for quick, throwaway functions.(e.g inside other functions)
# commonly used with functions like map(),filter(),and sorted().

#3. Traditional function vs lambda function.
#Normal:
#       def add(x,y):
#           return x + y
#Lambda function:
#       add = lambda x,y:x+y

#4. How lambda functions work.
# The expression automatically returns the result of the expression.
# You do not use return inside lambda.

#5. Example uses of lambda functions.
# A. Simple lambda.
square = lambda x: x * x
print(square(5))
# with map:
# map() applies a function to every item in a list.
nums = [1,2,3,4]
# using map() to apply a lambda function to each number in nums.
# lambda x: x*2 --> multiplies each element by 2.
# map() returns a map object, so we convert it to list.
squares = list(map(lambda x: x * 2,nums)) 
print(squares)

#6. Rules of lambda functions.
# only one expression.
# can have multiple arguments.
# no statements(like if statements inside) unless used as expression.
# useful for simple logic only.

#7. When should you use a lambda function?
# short, simple functions
# passed immediately as a parameter.
# functions not used elsewhere.

# Imp--> If a function is used more than once or is complex, use a normal function(def) instead.