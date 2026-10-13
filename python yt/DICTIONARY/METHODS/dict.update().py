# inserts the specified items to the dictionary.
# dict.update({})

student = {
    "name" : "Abdu",
    "roll no" : 30,
    "subjects" : {
        "Acc" : 85,
        "stat" : 89,
        "eco" : 74,
    }
}
student.update({"City" :"AMD"})
print(student)