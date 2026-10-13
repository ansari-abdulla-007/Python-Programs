# Nested dictionary.

student = {
    "name" : "Abdu",
    "roll no" : 30,
    "subjects" : {
        "Acc" : 85,
        "stat" : 89,
        "eco" : 74,
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["stat"])