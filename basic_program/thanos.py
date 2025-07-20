# info = {
#     "key" : "value",
#     "name" : "mera ghar",
#     "learning" : "coding",
#     "age" : 31,
#     "is adult" : True,
#     "marks" : 99.99
# }

# print(info)


# info = {
#     "name" : "mera ghar",
#     "subjects" : ["python", "c","java"],
#     "topics" : ["dict", "set"],
#     "age" : 31,
#     "is adult" : True,
#     12.99: 99.99
# }

# info["name"] = "aaryan"
# info["surname"] = "verma"
# print(info)


# student = {
#     "name" : "aryan verma",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "maths" : 95
#     }
# }

# #nested dictionary

# print(student["subjects"]["chem"])


student = {
    "name" : "aryan verma",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 95
    }
}

# print(list(student.keys()))

# print(list(student.values()))

# print(list(student.items()))

# pairs = list(student.items())

# print(pairs[0])


print(student["name"])
print(student.get("name"))