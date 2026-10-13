# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b>a:
    pass
#python pass statement.
#The pass statement is a null operation-nothing happens when it executes its a place holder.
#why use pass statement?
#the pass statement is useful in several situations.
#when ypu creating a code structure but haven,t implemented the logic yet
#when a statement is required syntactically but no action is needed.
#As a placeholder for future code during developement.
#In empty functions or classes that you plan to implement later.


#pass in Development.
#during developement,you might want to sketch out your program structure before implementing the details.
#the pass statement allows you to do this without syntax errors.

age = 16
if age > 18:
    pass #add logic later.
else:
    print("Access granted")