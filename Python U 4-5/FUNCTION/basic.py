# What is a function?
# A function is a block of code that runs only when it is called.
# A function can return data(give something back) to the part of the code that called it.
# Functions help you avoid repeating the same code over and over.
# How to create and use a function..
# Here is a full code example with comments explaining each part:
# Define (create) a function named greet_user.
def greet_user(name):
    """this function takes one input(name) and
    returns a greeting string."""
    #create a greeting message.
    greeting = "Hello, " +name+ "!"
    # Return the greeting message to whoever called the function.
    return greeting
# Now we call the function with different names.
print(greet_user("Abduu"))
print(greet_user("Sahil"))

# Define another functions that does something without returning a value/.
def say_goodbye():
    """
    this function prints a goodbye messeage.
    it does not return any value explicitly.
    """
    print("Goodbye!!")
#call the function
say_goodbye()