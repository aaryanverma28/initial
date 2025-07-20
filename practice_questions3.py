movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))

print(movies)

list1 = [1, 2, 1]
list1 = ["m", "a", "a", "m", "p"]
list2 = [2, 3, 4]

copy_list1 = list1.copy()

copy_list1 = list2.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")

if(copy_list1 == list2):
    print("palindrome")

else:
    print("Not palindrome")


grade = ("C", "D","A","A", "B", "B", "A")
print(grade.count("A"))

grade = ["C", "D","A","A", "B", "B", "A"]
grade.sort()
print(grade)