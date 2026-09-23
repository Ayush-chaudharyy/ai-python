# QUESTION-1
language =["python","jave","c++","javascript","sql"]
print(language)
print(language[0])
print(language[-1])
print(type(language))

# QUESTION-2
lst = []
lst.append(input('Enter a food name:'))
lst.append(input('Enter a food name:'))
lst.append(input('Enter a food name:'))
lst.append(input('Enter a food name:'))
lst.append(input('Enter a food name:'))
print(lst)
print(len(lst))
print(lst[0])
print(lst[-1])


# QUESTION-3
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[0])
print(numbers[3])
print(numbers[-1])
print(numbers[-3])

# QUESTION-4
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[0:4])
print(numbers[:-4:-1])
print(numbers[2:5])
print(numbers[::2])
print(numbers[::-1])

# QUESTION-5
languages = ["Python", "Java", "C++", "SQL"]
languages[1] = 'JavaScript'
languages[-1] = 'MySQL'
print(languages)


# QUESTION-6
skills = ["Python", "SQL"]
skills.append('Pandas')
skills.append('NumPy')
skills.insert(1,'Machine Learning')
print(skills)


# QUESTION-7
languages = ["Python", "Java", "C++", "JavaScript", "SQL"]
languages.remove('Java')
languages.pop()
languages.pop(1)
print(languages)


# QUESTION-8
numbers = [10, 20, 10, 30, 40, 10, 50]
print(numbers.count(10))
print(numbers.index(30))
print(len(numbers))


# QUESTION-9
marks = [78, 45, 92, 61, 88, 55]
print(marks)
marks.sort()
print("Ascending order",marks)
marks.sort(reverse=True)
print("Descending order",marks)


# QUESTION-10
languages = ["Python", "Java", "C++", "JavaScript", "SQL"]
use = input('Enter a language:')
print('Language exists:',use in languages)
print('Language does not exists:',use not in languages)

# QUESTION-11
python_topics = ["Variables", "Strings", "Lists"]
math_topics = ["Algebra", "Statistics", "Calculus"]
all_topic = python_topics + math_topics
print(all_topic)
print(len(all_topic))

# QUESTION-12
a = [10, 20, 30]
b = a.copy()
print(b)
b.append(40)
print('a =',a)
print('b =',b)

# QUESTION-13
marks = [int(input('Enter marks1:')),
         int(input('Enter marks2:')),
         int(input('Enter marks3:')),
         int(input('Enter marks4:')),
         int(input('Enter marks5:'))]
print(marks)
print("Total marks:",sum(marks))
print('Average',sum(marks)/5)
print('Highest Marks',max(marks))
print('Highest Marks',min(marks))


# QUESTION-14
students = [
    ["Jayant", 85],
    ["Rahul", 72],
    ["Aman", 91]
]
print(students[0][0])
print(students[0][1])
print(students[2][0])
print(students[2][1])


# QUESTION-15
tech_skills = [input('Enter skill 1:'),
               input('Enter skill 2:'),
               input('Enter skill 3:'),
               input('Enter skill 4:'),
               input('Enter skill 5:'),]
print(tech_skills)
tech_skills.append('Python')
print(tech_skills)
tech_skills.pop()
print(tech_skills)
tech_skills.sort()
print(tech_skills)
print(tech_skills[0])
print(tech_skills[-1])
print(len(tech_skills))
print('Python' in tech_skills)


# QUESTION-16
language = ('Python','SQL','Pandas','NumPy','Machine Learning')
print(language)
print(language[0])
print(language[-1])
print(len(language))
print(type(language))


# QUESTION-17
numbers = (10, 20, 30, 40, 50, 60, 70)
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[0:4])
print(numbers[::-1])


# QUESTION-18
languages = ("Python", "Java", "C++")
new_tuple = ('Python','Javascript','C++')



# QUESTION-19
numbers = (10, 20, 10, 30, 10, 40, 50)
print(numbers.count(10))
print(numbers.index(30))

# QUESTION-20
skills = ("Python", "SQL", "Pandas", "NumPy")
print("Python" in skills)
print("Java" in skills)



# QUESTION-21
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
print("Length:",len(c))
print("First element:",c[0])
print("Last element:",c[-1])


# QUESTION-22
data = ("Python")
print(data*5)


# QUESTION-23
student = ("Jayant", 23, "MCA")
name,age,*coursea = student
print('Name:',name)
print('Age:',age)
print('Coursea:',*coursea)

# QUESTION-24
numbers = [10, 20, 30, 40, 50]
tup_num = tuple(numbers)
print(type(tup_num)) 
tup_num1 = list(numbers)
print(type(numbers))
tup_num1.append(60)
print(tup_num1)


# QUESTION-25
data = (input('Enter a name:'),
        str(input('Enter a age:')),
        input('Enter a course:'),
        input('Enter a university:'))
print(data)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print('Length:',len(data))
print('Mca' in data)
lst = list(data)
lst.append('AI/ML')
print(lst)
tup = tuple(lst)
print('Final Tuple:',tup)

# QUESTION-26
a = range(0,10)
print(type(a))
b = list(a)
print(b)

# QUESTION-27
text = range(5,11)
a = list(text)
print(a)

# QUESTION-28
# Even numbers
even_numbers = range(2, 21, 2)
print(list(even_numbers))

# Odd numbers
odd_numbers = range(1, 20, 2)
print(list(odd_numbers))


# QUESTION-29
text = range(10,0,-1)
a =list(text)
print(a)


# QUESTION-30
start = int(input('Enter u want to start:'))
stop = int(input('Enter u want to stop:'))
step = int(input('Enter u want step:'))
a = range(start,stop,step)
print(start)
print(stop)
print(step)
b = list(a)
print(b)
print('Length:',len(b))
print('First value:',a[0])
print('Last value:',a[-1])