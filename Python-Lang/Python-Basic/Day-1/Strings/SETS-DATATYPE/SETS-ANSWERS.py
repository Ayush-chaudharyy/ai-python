# question -1
lang = {"Python", "Java", "C++", "SQL", "Python"}
print("the sets: ",lang)
print("The length: ", len(lang))
print("Its Datatype",type(lang))

# question -2
user_lang = {
     input("Enter the language 1: "),
     input("Enter the language 2: "),
input("Enter the language 3: "),
     input("Enter the language 4: "),
     input("Enter the language 5: ")
}
print("Language: ", user_lang)
print(len(user_lang))

# question -3
skills = {"Python", "SQL", "Git"}
skills.add("Pandas")
skills.add("Numpy")
skills.discard("Git")
print(skills)

# question -4
skills = {"Python", "SQL", "Pandas", "NumPy"}
input_skills = input("Enter the skill: ")
print("Our skills is present:", input_skills in skills)
print("Our skills is does exiist:", input_skills not in skills)

# question -5
frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "Java"}
all_technilogies = frontend | backend
print(all_technilogies)

# question -6
student_a = {"Python", "SQL", "Git", "Docker"}
student_b = {"Python", "Java", "Git", "Linux"}
common_skills = student_a & student_b
print("Common skills in both student are: ",common_skills)

# question -7
student_a = {"Python", "SQL", "Git", "Docker"}
student_b = {"Python", "Java", "Git", "Linux"}
set_diff = student_a - student_b
print(set_diff)

# question -8
a = {"Python", "SQL", "Git"}
b = {"Python", "Java", "Docker"}
only_item = a ^ b
print(only_item)

# question -9 
required = {"Python", "SQL"}
skills = {"Python", "SQL", "Pandas", "NumPy", "Git"}
print(required.issubset(skills))
print(skills.issubset(required))

# question - 10
person_1 = {
    input("student 1 Skills 1 : "),
    input("student 1 Skills 2 : "),
    input("student 1 Skills 3 : "),
    input("student 1 Skills 4 : "),
    input("student 1 Skills 5 : ")
}
person_2 = {
    input("student 2 Skills 1 : "),
    input("student 2 Skills 2 : "),
    input("student 2 Skills 3 : "),
    input("student 2 Skills 4 : "),
    input("student 2 Skills 5 : ")
}
unique_skills = person_1 | person_2
print("Uniques Skills :",unique_skills)

common_skills = person_1 & person_2
print("Common Skkills: ", common_skills)

student_a_skills = person_1 - person_2
print("Student 1 skills :", student_a_skills)

student_b_skills = person_2 - person_1
print("Student 2 skills :", student_b_skills)

python_skill = person_1 & person_2
print("Python is common: ", "Python" in python_skill)