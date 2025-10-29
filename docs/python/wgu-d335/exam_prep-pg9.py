student = {"name": "Pharns", "age": 33, "major": "Cybersecurity", "gpa": 3.8}


new_major = input("Update your major: ")

student["major"] = new_major

print("Updated Student Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Major: {student['major']}")
print(f"GPA: {student['gpa']}")
