# 🐍 Python Dictionary — 15 Question Assessment

**Total Questions:** 15
**Difficulty:** Beginner → Intermediate → Practical

> **Instructions:** Solve all questions yourself in Python. Use `input()` wherever user input is requested. Try to write the logic yourself before looking for help.

---

## 🟢 Basic Dictionary Operations

### Q1. Dictionary Creation

Create a dictionary containing your basic student information:

* Name
* Age
* Course
* University
* City

Print:

1. The complete dictionary
2. The value of `Name`
3. The value of `Course`
4. The datatype of the dictionary

---

### Q2. User Input Dictionary

Take the following information from the user:

* Name
* Age
* Email
* Course

Store all four values in a dictionary.

Print the complete dictionary.

---

### Q3. Access Dictionary Values

Given:

```python
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA",
    "university": "Bennett University"
}
```

Print:

1. Name
2. Age
3. Course
4. University

Access the values using dictionary keys.

---

### Q4. Add New Items

Given:

```python
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA"
}
```

Add the following items:

```text
university → Bennett University
city → Ghaziabad
```

Print the updated dictionary.

---

### Q5. Update Existing Values

Given:

```python
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA",
    "city": "Delhi"
}
```

Update:

* Age → `24`
* Course → `"MCA AI/ML"`
* City → `"Ghaziabad"`

Print the updated dictionary.

---

## 🟡 Dictionary Methods & Operations

### Q6. `keys()`, `values()` and `items()`

Given:

```python
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA",
    "city": "Ghaziabad"
}
```

Print:

1. All keys
2. All values
3. All key-value pairs

Use:

```python
keys()
values()
items()
```

---

### Q7. Dictionary Membership

Given:

```python
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA"
}
```

Ask the user to enter a key.

Check:

1. Whether the key exists
2. Whether the key does not exist

Use `in` and `not in`.

---

### Q8. `get()` Method

Given:

```python
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA"
}
```

Ask the user for a key.

Use `.get()` to retrieve its value.

If the key does not exist, display:

```text
Key not found
```

**Do not directly use `student[key]` for this question.**

---

### Q9. Remove Dictionary Items

Given:

```python
student = {
    "name": "Jayant",
    "age": 23,
    "course": "MCA",
    "city": "Ghaziabad"
}
```

Perform the following:

1. Remove `"city"` using `pop()`
2. Add `"email"`
3. Remove the last inserted item using `popitem()`
4. Print the final dictionary

---

### Q10. Dictionary Length & Clear

Create a dictionary containing **5 subjects and their marks**.

For example:

```python
marks = {
    "Python": 85,
    "SQL": 78,
    "Math": 72,
    "AI": 88,
    "ML": 81
}
```

Perform:

1. Print the number of subjects using `len()`
2. Print the complete dictionary
3. Remove all items using `clear()`
4. Print the dictionary again

---

## 🟠 Intermediate Dictionary Problems

### Q11. Student Marks Dictionary

Take marks for **5 subjects from the user**.

Store them in a dictionary:

```text
Subject → Marks
```

Then calculate and print:

* Total marks
* Average marks
* Highest marks
* Lowest marks

Example structure:

```python
{
    "Python": 85,
    "SQL": 78,
    "Math": 90,
    "AI": 82,
    "ML": 88
}
```

---

### Q12. Dictionary + List

Create:

```python
student = {
    "name": "Jayant",
    "course": "MCA",
    "skills": ["Python", "SQL", "Git"]
}
```

Perform:

1. Add `"Pandas"` to the skills
2. Add `"NumPy"` to the skills
3. Print the updated skills
4. Print the complete dictionary

---

### Q13. Dictionary + Set

Take **5 technical skills** from the user and store them in a set.

Then create a dictionary:

```text
name
course
skills
```

The `skills` value must be the set you created.

Print the complete dictionary.

Then:

1. Add another skill to the set
2. Remove one skill
3. Check whether `"Python"` exists
4. Print the final dictionary

---

### Q14. Nested Dictionary

Create the following dictionary:

```python
students = {
    "student1": {
        "name": "Jayant",
        "age": 23,
        "course": "MCA"
    },
    "student2": {
        "name": "Rahul",
        "age": 22,
        "course": "BCA"
    }
}
```

Print:

1. Student 1's name
2. Student 1's course
3. Student 2's name
4. Student 2's age

Then change Student 2's course to `"MCA"`.

Print the updated dictionary.

---

## 🔥 Q15. Final Challenge — Student Profile System

Create a **Student Profile System** using a dictionary.

Take the following from the user:

* Name
* Age
* Email
* Course
* University
* City
* 5 technical skills

Store the 5 skills inside a **set**, and then store that set inside the dictionary.

Your dictionary should conceptually look like:

```python
student = {
    "name": "...",
    "age": ...,
    "email": "...",
    "course": "...",
    "university": "...",
    "city": "...",
    "skills": {...}
}
```

Then perform the following operations:

1. Print the complete student profile
2. Print all keys
3. Print all values
4. Print all key-value pairs
5. Print the student's name
6. Print the student's skills
7. Add one new skill
8. Remove one skill
9. Check whether `"Python"` exists in the skills
10. Update the city
11. Add a new key `"experience"` with value `0`
12. Print the final dictionary

---

# 🎯 Concepts You Should Master

By the end of these 15 questions, you should be comfortable with:

```python
{}
[key]
get()
keys()
values()
items()
len()

in
not in

update
add / modify values

pop()
popitem()
clear()

nested dictionaries
dictionary + list
dictionary + set
```

### Final goal

You should be able to look at a problem and decide:

**"This information should be represented using a dictionary because I have key → value relationships."**

Complete **Q1–Q15** and send me your code. I'll evaluate each question separately with a **/10 score**, identify exactly where your logic/code can improve, and distinguish beginner mistakes from things that matter in real Python development.