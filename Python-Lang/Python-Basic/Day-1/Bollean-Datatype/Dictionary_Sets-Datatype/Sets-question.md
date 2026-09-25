# 🐍 Python Sets & Dictionaries Assessment

**Total: 20 Questions**

* Sets → 10 questions
* Dictionaries → 10 questions
* Difficulty → Beginner → Intermediate → Practical

---

# 🟢 PART A — SETS

## 10 Questions

### Q1. Set Creation & Basic Operations

Create a set containing:

```text
Python, Java, C++, SQL, Python
```

Print:

* The set
* Its length
* Its datatype

Observe what happens to the duplicate `"Python"`.

---

### Q2. User Input & Set

Ask the user to enter **5 programming languages**.

Store them in a set.

Print:

* The set
* Number of unique languages

---

### Q3. Add & Remove

Given:

```python
skills = {"Python", "SQL", "Git"}
```

Perform:

1. Add `"Pandas"`
2. Add `"NumPy"`
3. Remove `"Git"`
4. Print the final set

---

### Q4. Set Membership

Given:

```python
skills = {"Python", "SQL", "Pandas", "NumPy"}
```

Ask the user for a skill.

Check whether the skill:

* Exists in the set
* Does not exist in the set

Use `in` and `not in`.

---

### Q5. Union

Given:

```python
frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "Java"}
```

Create a set containing **all technologies** from both sets.

Use the appropriate set operation.

---

### Q6. Intersection

Given:

```python
student_a = {"Python", "SQL", "Git", "Docker"}
student_b = {"Python", "Java", "Git", "Linux"}
```

Find the skills that **both students have**.

---

### Q7. Difference

Using the same sets from Q6, find:

1. Skills only Student A has
2. Skills only Student B has

Use set difference.

---

### Q8. Symmetric Difference

Given:

```python
a = {"Python", "SQL", "Git"}
b = {"Python", "Java", "Docker"}
```

Find the skills that are present in **only one of the two sets**, but not both.

---

### Q9. Subset & Superset

Given:

```python
required = {"Python", "SQL"}
skills = {"Python", "SQL", "Pandas", "NumPy", "Git"}
```

Check:

1. Is `required` a subset of `skills`?
2. Is `skills` a superset of `required`?

Print both Boolean results.

---

### Q10. 🔥 Set Challenge — Common Skills

Take the skills of two students from the user.

For each student, ask for **5 skills** and store them in separate sets.

Then display:

1. All unique skills possessed by both students
2. Skills common to both
3. Skills only Student 1 has
4. Skills only Student 2 has
5. Whether both students have `"Python"`

---