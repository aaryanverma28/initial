def print_marks_info(marks):
    """Prints information about the marks list."""
    print(f"Marks List: {marks}")
    print(f"Number of Marks: {len(marks)}")
    if marks:
        print("First Mark:", marks[0])
        print("Second Mark:", marks[1] if len(marks) > 1 else "N/A")
        print("Marks from index 1 to 3:", marks[1:4])
        print("Marks from index 1 to end:", marks[1:])
        print("Marks up to index 3:", marks[:4])
        print("Marks from -3 to -1:", marks[-3:-1])
    else:
        print("No marks available.")

def print_student_info(student):
    """Prints information about the student."""
    if len(student) >= 4:
        name, score, age, city = student
        print(f"Student Name: {name}")
        print(f"Score: {score}")
        print(f"Age: {age}")
        print(f"City: {city}")
    else:
        print("Incomplete student information:", student)

if __name__ == "__main__":
    marks = [88, 12]
    student = ["Aryan", 91.5, 25, "Muzaffarnagar"]

    print("=== Student Information ===")
    print_student_info(student)
    print("\n=== Marks Information ===")
    print_marks_info(marks)

list = [5,4,3,2]
list.append(1)
print(list)

list = [1,2,3,4,5]
list = ["litchi", "apple","watermelon"]
list.sort()
list.sort(reverse=True)
print(list)

list = ["a", "b","d", "c", "e", "f"]
list.reverse()
print(list)

list = [2, 1, 3]
list.insert(1, 6)
print(list) 

list = [2, 1, 3, 1]
list.remove(1)
print(list)

list = [2, 1, 3, 1]
list.pop(2)
  