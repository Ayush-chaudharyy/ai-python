# QUESTION-1
Stus_info = {"Name":"Ayush",
             "Age":21,
             "Course":"M.C.A",
             "University":"IMS",
             "City":"Hapur"}
print(Stus_info)
print(Stus_info.get("Name"))
print(Stus_info.get("Course"))
print(type(Stus_info))

# QUESTION-2
user_detail = {
    "Name" : input("Enter a Name:"),
    "Age" : input("Enter a Age:"),
    "Email" : input("Enter a Email:"),
    "Course" : input("Enter a Course:")}
print(user_detail)

# QUESTION-3
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA",
    "university": "Bennett University"
}
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))
print(student.get("university"))


# QUESTION-4
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA"
}
student["university"] = "bennett university"
student["city"] = "ghaziabad"
print(student)

# QUESTION-5
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA",
    "city": "Delhi"
}
student["age"] = 24
student["course"] = "AI/ML"
student["city"] = "ghaziabad"
print(student)


# QUESTION-6
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA",
    "city": "Ghaziabad"
}
print(student.keys())
print(student.items())
print(student.values())

# QUESTION-7
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA"
}
user_key = input("Enter a key:")
print(user_key in student)
print(user_key not in student)

# QUESTION-8
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA"
}
user_key = input("Enter a key:")
print("key not found:",user_key in student)

# QUESTION-9
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA",
    "city": "Ghaziabad"
}
student.pop("city")
print(student)
student["emali"] = "ayu1233@gmail.com"
print(student)
student.popitem()
print(student)

# QUESTION-10
marks = {
    "Python": 85,
    "SQL": 78,
    "Math": 72,
    "AI": 88,
    "ML": 81
}
print(len(marks))
print(marks)
print(marks.clear())
print(marks)