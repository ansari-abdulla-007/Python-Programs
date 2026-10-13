# Returns the key according to value.


dict = {
    "name" : "Abduu",
    "age" : "18",
    "subject" :["python","c","fos"],
}

print(dict["name"])
print(dict.get("name"))

print(dict["name2"]) #gives error.
print(dict.get("name2")) #no error -> None