# Write a Python program to:
# • Create a dictionary of subjects
# • Remove one subject using the pop() method
# • Display the remaining dictionary.
subjects = {
    "Maths":90,
    "English":85,
    "Hindi":78
}
subjects.pop("English")
print(subjects)