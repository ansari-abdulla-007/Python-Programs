#define a function that takes two regular arguments (parameters).
def greet(first_name,last_name):
    #print a greeting combining the two passed arguments.
    print("Hello, "+ first_name +" " + last_name + "!")
#call the function with two arguments.
greet("Alice","Johnson")

#if you call the function with wrong number of arguments it will give an error.
#example (uncommenting will cause an error):
# greet("alice") #missing the second argument.
# greet("alice","johnson","extra") # too many arguments.

# define a function with a default parameter value.
def greet_with_country(name,country="India"):
    #if country is not provided, it uses the default "india".
    print("Hello, "+ name + " from "+ country +"!")
#calling the both arguments.
greet_with_country("Aryan","Thailand")
#calling with only name - uses default country.
greet_with_country("Abduu")
greet_with_country("Sahil")
greet_with_country("Jimi")