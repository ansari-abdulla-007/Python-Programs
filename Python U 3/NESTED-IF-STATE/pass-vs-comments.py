#pass vs comments.
# a comment is ignored by python, but pass is an actual statement that gets executed(though it does nothing).
# you need pass where python expects a statement, not just a comment.

# this will cause an error(empty code block):
score = 85
if score > 90:
    pass
print("score process")

#2.
#pass with multiple conditions.
# you can use pass in any branch of an if-else- statement.
# using pass in different branches:

value = 50
if value < 0:
    print("Negative value")
elif value == 0:
    pass #zero case - no action
else:
    print("positive value")

#3.
#pass in other contexts.
#while we focus on pass with if statements here, its also commonly used with loops, functions, and classes.

#using pass with functions:
def calculate_discount(price):
    pass #implement discount logic later.