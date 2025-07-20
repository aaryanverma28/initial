info = {
      "name" : "aaryan",
      "subjects" : ["python", "C++", "Java"],
      "topics" : ("dict", "sets"),
     "learning" : "python",
     "age" : 38,    
     "is_adult" : True,
     "marks" : 95.8
}

print(type(info))
info["surname"] = "verma"
print(info)

null_dict = {}
null_dict["name"] = "aaryan"
print(null_dict)

student = {
    "name" : "pihu",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 95
    }
}

# nested dictionary

print(student)


student = {
    "name" : "pihu",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 95
    }
}

print(len(list(student.keys())))

print(list(student.values()))

print(list(student.items()))

pairs = list(student.items())
print(pairs[1])

print(student.get("name2")) #no error -> None

new_dict = {"name" : "ram", "age" : 18}
student.update(new_dict)
print(student)