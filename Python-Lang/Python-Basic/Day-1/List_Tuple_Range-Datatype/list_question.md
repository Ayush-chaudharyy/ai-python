# 🐍 Python Sequential Datatypes Assessment

## Topics

* Lists — 15 Questions
* Tuples — 10 Questions
* Range — 5 Questions

**Total: 30 Questions**

> **Instructions:** Solve everything yourself in Python.
> Use `input()` wherever the question asks for user input.
> Try to avoid `if/else` unless the question specifically requires it.

---

# 🟢 PART A — LISTS

## 15 Questions

### Q1. Create and Access a List

Create a list containing 5 programming languages:

```text
Python, Java, C++, JavaScript, SQL
```

Print:

1. The complete list
2. The first element
3. The last element
4. The datatype of the list

---

### Q2. User Input List

Ask the user to enter **5 favorite foods**, one at a time.

Store them in a list and print:

* Complete list
* Number of foods
* First food
* Last food

---

### Q3. List Indexing

Given:

```python
numbers = [10, 20, 30, 40, 50, 60, 70]
```

Print:

1. Element at index `0`
2. Element at index `3`
3. Element at index `-1`
4. Element at index `-3`

---

### Q4. List Slicing

Given:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
```

Print:

1. First 4 elements
2. Last 3 elements
3. Elements from index `2` to `5`
4. Every second element
5. The reversed list using slicing

---

### Q5. Modifying List Elements

Given:

```python
languages = ["Python", "Java", "C++", "SQL"]
```

Replace:

* `"Java"` with `"JavaScript"`
* `"SQL"` with `"MySQL"`

Print the updated list.

---

### Q6. Adding Elements

Create:

```python
skills = ["Python", "SQL"]
```

Add:

* `"Pandas"` using `append()`
* `"NumPy"` using `append()`
* `"Machine Learning"` using `insert()` at index `1`

Print the final list.

---

### Q7. Removing Elements

Given:

```python
languages = ["Python", "Java", "C++", "JavaScript", "SQL"]
```

Perform the following:

1. Remove `"Java"`
2. Remove the last element using `pop()`
3. Remove the element at index `1` using `pop()`

Print the list after each operation.

---

### Q8. List Methods

Create:

```python
numbers = [10, 20, 10, 30, 40, 10, 50]
```

Find:

1. Number of times `10` occurs
2. Index of the first `30`
3. Total number of elements

Use appropriate list methods/functions.

---

### Q9. Sorting a List

Given:

```python
marks = [78, 45, 92, 61, 88, 55]
```

Create a program that:

1. Prints the original list
2. Sorts it in ascending order
3. Sorts it in descending order

Use list methods.

---

### Q10. List Membership

Take a list of 5 programming languages.

Ask the user for a language to search for.

Print Boolean results for:

```text
Language exists: True/False
Language does not exist: True/False
```

Use:

```python
in
not in
```

---

### Q11. Combining Lists

Create:

```python
python_topics = ["Variables", "Strings", "Lists"]
math_topics = ["Algebra", "Statistics", "Calculus"]
```

Create a third list containing all elements from both lists.

Then print:

* Combined list
* Length of combined list

---

### Q12. Copy vs Reference

Create:

```python
a = [10, 20, 30]
```

Create another list `b` from `a`.

Modify `b` by adding `40`.

Print both `a` and `b`.

Then repeat the experiment using:

```python
b = a.copy()
```

Observe the difference.

---

### Q13. List of User Marks

Ask the user to enter marks for **5 subjects**.

Store them in a list.

Calculate:

* Total marks
* Average marks
* Highest mark
* Lowest mark

Use appropriate built-in functions.

---

### Q14. Nested List

Create the following nested list:

```python
students = [
    ["Jayant", 85],
    ["Rahul", 72],
    ["Aman", 91]
]
```

Print:

1. Jayant's name
2. Jayant's marks
3. Aman’s name
4. Aman’s marks

Then change Rahul's marks to `80`.

Print the updated list.

---

### Q15. 🔥 List Challenge — Student Skills

Take the user's **5 technical skills** as input and store them in a list.

Then:

1. Print the original list
2. Add `"Python"` if it isn't already present
3. Remove the last skill
4. Sort the list alphabetically
5. Print the first skill
6. Print the last skill
7. Print the total number of skills
8. Check whether `"Python"` exists in the final list

---

# 🟡 PART B — TUPLES



### Q16. Create and Access a Tuple

Create a tuple containing:

```text
Python, SQL, Pandas, NumPy, Machine Learning
```

Print:

1. Complete tuple
2. First element
3. Last element
4. Length
5. Datatype

---

### Q17. Tuple Indexing & Slicing

Given:

```python
numbers = (10, 20, 30, 40, 50, 60, 70)
```

Print:

1. First element
2. Last element
3. Element at index `3`
4. Last 3 elements
5. First 4 elements
6. Reversed tuple using slicing

---

### Q18. Tuple Immutability

Create:

```python
languages = ("Python", "Java", "C++")
```

Try to change `"Java"` to `"JavaScript"`.

Observe and understand what happens.

Then create a **new tuple** containing:

```text
Python, JavaScript, C++
```

---

### Q19. Tuple Methods

Given:

```python
numbers = (10, 20, 10, 30, 10, 40, 50)
```

Find:

1. How many times `10` appears
2. The index of the first `30`

Use appropriate tuple methods.

---

### Q20. Tuple Membership

Given:

```python
skills = ("Python", "SQL", "Pandas", "NumPy")
```

Check whether:

* `"Python"` exists
* `"Java"` exists

Use `in` and `not in`.

---

### Q21. Tuple Concatenation

Create:

```python
a = (1, 2, 3)
b = (4, 5, 6)
```

Create a third tuple containing all values from `a` and `b`.

Then print:

* Combined tuple
* Length
* First element
* Last element

---

### Q22. Tuple Repetition

Create:

```python
data = ("Python",)
```

Repeat the tuple **5 times** using the repetition operator.

Print the result.

> Pay attention to why the comma is required when creating a one-element tuple.

---

### Q23. Tuple Unpacking

Create:

```python
student = ("Jayant", 23, "MCA")
```

Unpack the tuple into:

```text
name
age
coursea
```

Then print each variable separately.

---

### Q24. Convert Between List and Tuple

Create:

```python
numbers = [10, 20, 30, 40, 50]
```

1. Convert the list into a tuple.
2. Print its datatype.
3. Convert the tuple back into a list.
4. Add `60` to the list.
5. Print the final list.

---

### Q25. 🔥 Tuple Challenge — Student Record

Create a tuple containing:

```text
Name
Age
Course
University
```

Take all four values from the user.

Then:

1. Print the complete tuple
2. Print each value using indexing
3. Print the length
4. Check whether `"MCA"` exists in the tuple
5. Convert the tuple to a list
6. Add `"AI/ML"` to the list
7. Convert it back to a tuple
8. Print the final tuple

---

# 🔵 PART C — RANGE

## 5 Questions

### Q26. Basic Range

Create a range from `0` to `10`.

Convert it into a list and print the result.

Also print its datatype before conversion.

---

### Q27. Range with Start and Stop

Create a range that generates:

```text
5 6 7 8 9 10
```

Convert it into a list and print it.

---

### Q28. Range with Step

Create a range that generates:

```text
2 4 6 8 10 12 14 16 18 20
```

Convert it into a list and print it.

Then create another range that generates the odd numbers from `1` to `19`.

---

### Q29. Reverse Range

Use `range()` to generate:

```text
10 9 8 7 6 5 4 3 2 1
```

Convert the range to a list and print it.

**Do not manually write the numbers.**

---

### Q30. 🔥 Final Range Challenge

Take two integers from the user:

```text
start
stop
```

Then take a third integer:

```text
step
```

Create a `range()` using these three values.

Print:

1. The range object
2. The range converted into a list
3. The number of values generated using `len()`
4. The first value if the range contains values
5. The last value if the range contains values

Test your program with different combinations of:

```text
start < stop
start > stop
positive step
negative step
```

---

# 🎯 What You Should Know After This Assessment

After completing all 30 questions, you should be comfortable with:

### Lists

```python
[]
indexing
slicing
append()
insert()
remove()
pop()
count()
index()
sort()
copy()
in
not in
+
*
len()
max()
min()
sum()
```

### Tuples

```python
()
indexing
slicing
count()
index()
+
*
in
not in
unpacking
list() 
tuple()
```

### Range

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

And especially understand the difference between:

```python
list
tuple
range
```

in terms of **mutability, indexing, slicing, and common use cases**.

**Do not rush into the next datatype.** Complete these 30 questions first and send me your code. I'll evaluate them question-by-question and give you a score, mistakes, and practical code-quality feedback.