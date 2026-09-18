# QUESTION-1
name = 'AYUSH CHOUDHARY'
print(f'My name is {name}')
print(type(name))

# QUESTION-2
name = 'Ayush'
course = 'MCA'
university = 'Bennett'
print('Name:',name)
print('Course:',course)
print('University:',university)


# QUESTION-3
first_name = "Jayant"
last_name = "Chaudhary"
full_name = first_name +' '+last_name
print(full_name)

# QUESTION-4
word = 'Python' 
print(word*5)


# QUESTION-5
user_data = str(input('Enter a string:'))
print(user_data)
print('Length of string is:',len(user_data))

# QUESTION-6
text = 'PYTHON'
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# QUESTION-7
text = "PROGRAMMING"
print(text[-1])
print(text[-2])
print(text[-3])


# QUESTION-8
text = "PYTHON"
print(text[0])
print(text[2])
print(text[-1])
print(text[-2])

# QUESTION-9
text = "PROGRAMMING"
print(text[:4])
print(text[-4:])
print(text[2:7])

# QUESTION-10
text = str(input('Enter a string:'))
print(text[::-1])


# QUESTION-11
text = str(input('Enter a string:'))
print(text)
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

# QUESTION-12
text = "   Python is Amazing   "
print(len(text))
new_txt = text.strip()
print(len(new_txt))


# QUESTION-13
text = "I love Java"
print(text.replace('Java','Python'))

# QUESTION-14
text = "Python is easy to learn and Python is powerful"
print(text.find('Python'))
print(text.find('Powerful'))

# QUESTION-15
text = str(input('Enter a string:'))
character = str(input('Enter a character:'))
count = text.count(character)
print(count)


# QUESTION-16
text = str(input('Enter a string:'))
word = str(input('Enter a word:'))
print(word in text)


# QUESTION-17
file_name = str(input('Enter a file name:'))
print("Starts with data:",file_name.startswith('data'),"\nEnds with .csv:",file_name.endswith('.csv'))


# QUESTION-18
sentence = input('Enter a scentence:-')
word = sentence.split()
print(word)
print(len(word))

# QUESTION-19
first_name = str(input('Enter first name:-'))
last_name = str(input('Enter last name:-'))
year = int(input('Enter a year:-'))
year_st = str(year)
user_name = first_name +"."+ last_name + year_st
print('Username:',user_name.lower())

# QUESTION-20
text = str(input('Enter a text:'))
Full_Name = str(input('Enter a full name:-'))
College_Name = str(input('Enter a college name:-'))
Course = str(input('Enter a course:-'))
City = str(input('Enter your city:-'))
Email = str(input('Enter a email:-'))
print('====================================')
print('             STUDENT PROFILE        ')
print('====================================')
print('Name :-',Full_Name)
print('College :-',College_Name)
print('Course :-',Course)
print('City :-',City)
print('Email :-',Email)
print('====================================')

# PART-2
print('Name :-',Full_Name.upper())
print('Name :-',Full_Name.lower())
print('Number of characters:-',len(Full_Name))
print('First character of the name:-',Full_Name[0])
print('Last character of the name:-',Full_Name[-1])
print('@' in Email)
print(Email.endswith('.com'))
print(Full_Name.replace(' ','_'))