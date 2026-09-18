# 🐍 Python String Data Type Assessment — 20 Questions

*Total Questions:* 20
*Total Marks:* 200
*Marks per Question:* 10

## 📚 Topics Covered

* String creation
* String variables
* Single / double / triple quotes
* Indexing
* Negative indexing
* String slicing
* String concatenation
* String repetition
* len()
* Membership operators: in, not in
* String methods
* upper()
* lower()
* capitalize()
* title()
* swapcase()
* strip()
* replace()
* find()
* count()
* startswith()
* endswith()
* split()
* join()
* Basic string formatting

> *Rule:* Try to solve every question yourself. Don't look up solutions. If a method hasn't been taught yet, mark the question SKIP and continue.

---

# 🟢 LEVEL 1 — STRING FUNDAMENTALS

## Q1. Create and Print a String

Create a variable called name and store your full name in it.

Print:

text
My name is [your name].


Also print the data type of the variable using:

python
type()


---

## Q2. Multiple Strings

Create three string variables:

text
name
course
university


Store appropriate values and print them in separate lines.

Example:

text
Name: Jayant
Course: MCA AI/ML
University: Bennett University


---

## Q3. String Concatenation

Create two variables:

python
first_name = "Jayant"
last_name = "Chaudhary"


Join them together to produce:

text
Jayant Chaudhary


Use the string concatenation operator.

---

## Q4. String Repetition

Create:

python
word = "Python"


Use the string repetition operator to print:

text
PythonPythonPython


Then print the word 5 times.

---

## Q5. Find String Length

Take a string from the user.

Print:

text
Original String: ______
Length: ______


Use the appropriate built-in function to find the number of characters.

---

# 🟢 LEVEL 2 — STRING INDEXING & SLICING

## Q6. Positive Indexing

Given:

python
text = "PYTHON"


Print each character separately using positive indexing:

text
P
Y
T
H
O
N


Do not use a loop.

---

## Q7. Negative Indexing

Given:

python
text = "PROGRAMMING"


Use negative indexing to print:

1. Last character
2. Second-last character
3. Third-last character

---

## Q8. Extract Characters

Given:

python
text = "PYTHON"


Use indexing to print:

text
First character
Third character
Last character
Second-last character


---

## Q9. Basic Slicing

Given:

python
text = "PROGRAMMING"


Use slicing to extract:

text
First 4 characters
Last 4 characters
Characters from index 2 to 6


---

## Q10. Reverse a String

Take a string from the user and reverse it using *string slicing*.

Example:

text
Input: Python
Output: nohtyP


Do not use a loop.

---

# 🟡 LEVEL 3 — STRING OPERATIONS & METHODS

## Q11. Change String Case

Take a string from the user.

Print:

text
Original
UPPERCASE
lowercase
Capitalized
Title Case
Swap Case


Use the appropriate string methods.

---

## Q12. Remove Extra Spaces

Given:

python
text = "   Python is Amazing   "


Remove the unnecessary spaces from the beginning and end.

Print:

text
Python is Amazing


Also print the length of the string:

* Before removing spaces
* After removing spaces

---

## Q13. Replace Characters

Given:

python
text = "I love Java"


Replace "Java" with "Python".

Expected output:

text
I love Python


---

## Q14. Find a Word

Given:

python
text = "Python is easy to learn and Python is powerful"


Find the position/index of the *first occurrence* of "Python".

Also find the position/index of "powerful".

---

## Q15. Count Characters

Take a string from the user.

Ask the user for a character.

Count how many times that character appears in the string.

Example:

text
Enter string: programming
Enter character: m

m appears 2 times.


---

# 🟡 LEVEL 4 — MEMBERSHIP & STRING ANALYSIS

## Q16. Membership Test

Take a sentence from the user.

Ask the user for a word.

Check whether the word exists in the sentence using:

python
in


Print an appropriate result.

Example:

text
Sentence: Python is easy to learn
Word: Python

Result: Python exists in the sentence.


Also test the opposite case.

---

## Q17. Starts With / Ends With

Take a filename from the user.

Check whether:

* It starts with "data"
* It ends with ".csv"

Example:

text
Filename: data_science.csv

Starts with data: True
Ends with .csv: True


Use the appropriate string methods.

---

## Q18. Split a Sentence

Take a sentence from the user.

Split the sentence into individual words.

Example:

text
Input:
Python is easy to learn

Output:
['Python', 'is', 'easy', 'to', 'learn']


Also print the total number of words.

---

# 🟠 LEVEL 5 — STRING CHALLENGES

## Q19. Username Generator

Take the following information from the user:

text
First Name
Last Name
Year of Birth


Create a username using string operations.

For example:

text
First Name: Jayant
Last Name: Chaudhary
Year: 2003


Possible output:

text
Username: jayant.chaudhary2003


### Requirements

* Convert the name to lowercase.
* Join the first and last name.
* Add the birth year.
* Don't manually type the final username.

---

# 🔴 Q20. FINAL BOSS — Student Profile

Create a program that takes the following information from the user:

text
Full Name
College Name
Course
City
Email


Your program should generate a clean student profile.

Example:

text
====================================
          STUDENT PROFILE
====================================

Name      : Jayant Chaudhary
College   : Bennett University
Course    : MCA AI/ML
City      : Greater Noida
Email     : jayantd@example.com

====================================


### Your program must also perform the following string operations:

1. Print the student's name in uppercase.
2. Print the student's name in lowercase.
3. Print the number of characters in the student's full name.
4. Print the first character of the name.
5. Print the last character of the name.
6. Check whether the email contains "@".
7. Check whether the email ends with ".com".
8. Replace spaces in the name with _.

### Example

text
Name Uppercase : AYUSH KUMAR
Name Lowercase : ayush kumar
Name Length    : 17
First Character: J
Last Character : Y
Contains @     : True
Ends with .com : True
Username Name  : Ayush_Kumar