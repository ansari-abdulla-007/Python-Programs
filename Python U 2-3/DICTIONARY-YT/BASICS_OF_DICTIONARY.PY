# Dictionary are used to store data values in  key:value pairs they are unordered(without index), mutable & don't allow duplicate keys.

dict = {
    "name" : "Abduu",
    "age" : "18",
    "subject" :["python","c","fos"],
}

print(dict)
print(dict["subject"])
print(type(dict))

# We can also add new key:value easily.
dict["surname"] = "Ansari"
# We can assign new value in a key.
dict["name"] = "Abdulla"
print(dict)