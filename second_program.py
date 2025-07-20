str = "Hey this ia aaryan verma.\nI'm a learning python programe."
print(str)

str1 = "Verma"
str2 = "home"
final_str = str1 + str2
print(final_str)

str1 = "Verma"
len = len(str1)
print(len)

str2 = "home"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2
print(final_str)
print(len(final_str))

str = "saraswati mandi"
ch = str[0]
print(ch)
print(str[1])

str = "saraswati mandir"
print(str[1:4])
print(str[:4])
print(str[1:])

str = "apple"
print(str[-3:-1])

str = "I'm studying python programme."
print(str.endswith("mme"))

str = "I'm studying a python programming from youtube."
str = str.capitalize()
print(str)

str = "I'm studying a python programming from youtube."
print(str.replace("python", "java"))

str = "I'm studant from B.tech camputer science engg."
print(str.find("gg"))

print(str.count("e"))

age = 25

if(age >= 18):
    print("can vote.")
    print("can drive.")

light = "yellow"

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")

print("end of program")

num = 10
if(num > 5):
    print("greater than 5")
elif(num > 6):
    print("less than 6")

else:
    print("light is broken")
 
age = 30

if(age >= 18):
    print("can vote.") #indentation
else:    
    print("can't vote.")

marks = int(input("Enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student ->" , grade)

age = 90

# nesting
if(age >= 18):
    if(age >= 85):
        print("can't drive.")
    else:
        print("can drive.")
else:
        print("can't drive")
