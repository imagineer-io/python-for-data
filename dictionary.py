student = {
    "name": "Marco",
    "age": 30,
    "nationality": "Korea",
    "married": True
}

# get value
print(student["name"])

# add key and value
student["score"] = 50
print(student)

# remove key
del student["age"]
print(student)