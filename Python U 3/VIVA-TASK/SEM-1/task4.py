# Write a Python program to:
# 1. Create a list and modify one of its elements.
# 2. Create a tuple and attempt to modify one element.
# 3. Observe and comment the result.
my_list = ["Ansari",18,"python learner"]
my_tuple = ("Abdulla","Sahil",)
my_list[1]=19
print(my_list)
print(type(my_list))
my_tuple[0]="Abduu"
print(my_tuple)
# Tuple are immutable so we cannot change or modify element in tuple.