# QUESTION-1
language = {'Python','Java','C++','Python'}
print(language)
print('Length:',len(language))
print(type(language))


# QUESTION-2
language = {input('Enter a Programming language1:-'),
            input('Enter a Programming language2:-'),
            input('Enter a Programming language3:-'),
            input('Enter a Programming language4:-'),
            input('Enter a Programming language5:-'),}
print(language)
print('No. of unique language:',len(language))


# QUESTION-3
skills = {"Python", "SQL", "Git"}
skills.update(['Pandas','Numpy'])
print(skills)
skills.remove('Git')
print(skills)


# QUESTION-4
skills = {"Python", "SQL", "Pandas", "NumPy"}
user = input('Enter a skill:')
print('Exist in sets',user in skills)
print('Not Exist in set',user not in skills)


# QUESTION-5
frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "Java"}

print(frontend.union(backend))


# QUESTION-6
student_a = {"Python", "SQL", "Git", "Docker"}
student_b = {"Python", "Java", "Git", "Linux"}
print(student_a.intersection(student_b))

# QUESTION-7
student_a = {"Python", "SQL", "Git", "Docker"}
student_b = {"Python", "Java", "Git", "Linux"}
print(student_a.difference(student_b))
print(student_b.difference(student_a))

# QUESTION-8
a = {"Python", "SQL", "Git"}
b = {"Python", "Java", "Docker"}
print(a.symmetric_difference(b))

# QUESTION-9
required = {"Python", "SQL"}
skills = {"Python", "SQL", "Pandas", "NumPy", "Git"}
print('Is `required` a subset of `skills',required.issubset(skills))
print('Is `skills` a superset of `required',skills.issuperset(required))

# QUESTION-10
student_1 = {input('Enter a skill 1:'),
             input('Enter a skill 2:'),
             input('Enter a skill 3:'),
             input('Enter a skill 4:'),
             input('Enter a skill 5:'),}

student_2 = {input('Enter a skill 1:'),
             input('Enter a skill 2:'),
             input('Enter a skill 3:'),
             input('Enter a skill 4:'),
             input('Enter a skill 5:'),}

print('All unique skills possessed by both students',student_1.symmetric_difference(student_2))
print('Skills common to both',student_1.intersection(student_2))
print(student_2.difference(student_1))
print(student_1.difference(student_2))
print('Python' in student_1 in student_2)
