# 🐍 Python Boolean & Boolean Operations — Assessment

**Total Questions:** 20
**Topic:** Boolean Datatype & Boolean Operations
**Difficulty:** Beginner → Intermediate

> **Instructions:** Solve all questions yourself. Don't use ChatGPT or Google while solving. Write and run your code in VS Code.

---

## 🟢 Section 1 — Boolean Basics

### Q1. Creating Boolean Values

Create two variables:

* `is_student = True`
* `has_job = False`

Print both variables and their types.

---

### Q2. Boolean Conversion

Take a value from the user and convert it into a Boolean using `bool()`.

Test your program with:

* `0`
* `1`
* an empty string `""`
* a non-empty string

Observe the output.

---

### Q3. Comparison → Boolean

Create two variables:

```python
a = 25
b = 40
```

Check and print whether:

* `a` is greater than `b`
* `a` is less than `b`
* `a` is equal to `b`

---

### Q4. Equality & Inequality

Take two numbers from the user and check:

* Are they equal?
* Are they different?

Print both Boolean results.

---

### Q5. Even or Odd

Take an integer from the user.

Create a Boolean expression that checks whether the number is even.

Example:

```text
Enter number: 24
Is even: True
```

---

## 🟡 Section 2 — Comparison Operators

### Q6. Age Eligibility

Take the user's age.

Create a Boolean variable:

```text
is_adult
```

It should be `True` if age is **18 or above**, otherwise `False`.

---

### Q7. Passing Marks

Take marks from the user.

A student passes if the marks are **40 or above**.

Create and print:

```text
Passed: True/False
```

---

### Q8. Number Range

Take a number from the user.

Check whether the number is between **10 and 50**, including both 10 and 50.

Example:

```text
Enter number: 25
Is between 10 and 50: True
```

---

### Q9. Greater Number

Take two numbers from the user.

Create Boolean expressions to determine:

* Is the first number greater?
* Is the second number greater?
* Are they equal?

---

### Q10. Temperature Check

Take the current temperature as input.

Check whether the temperature is:

* below 10°C
* between 10°C and 30°C
* above 30°C

Print the Boolean result for each condition.

---

## 🟠 Section 3 — `and`, `or`, `not`

### Q11. `and` Operator

Create:

```python
age = 23
has_id = True
```

A person is eligible if:

* age is 18 or above **AND**
* they have an ID.

Create a Boolean expression to check eligibility.

---

### Q12. `or` Operator

A student can enter a competition if they have **either**:

* a student ID
* OR a valid registration number.

Create Boolean variables for both and use `or` to determine eligibility.

---

### Q13. `not` Operator

Create:

```python
is_raining = False
```

Use the `not` operator to determine whether it is **not raining**.

Print the result.

---

### Q14. Combine `and` + `or`

A person can apply for a job if:

* they are at least 18 years old **AND**
* they have either a degree **OR** relevant experience.

Take all required values from the user and create one Boolean expression.

---

### Q15. Combine `not` + `and`

Create:

```python
is_banned = False
has_valid_ticket = True
```

A person can enter an event only if:

* they are **not banned**
* AND they have a valid ticket.

Create the Boolean expression.

---

## 🔴 Section 4 — Logic & Real-World Problems

### Q16. Login Validation

Create:

```python
correct_username = "admin"
correct_password = "1234"
```

Take username and password from the user.

Create a Boolean expression that returns `True` only when:

* username is correct **AND**
* password is correct.

Example:

```text
Login successful: True
```

---

### Q17. College Admission Eligibility

Take the following from the user:

* age
* percentage
* entrance exam status (`True`/`False`)

A student is eligible if:

* age is at least 17
* percentage is at least 60
* entrance exam is cleared

Use Boolean operators to create one final eligibility result.

---

### Q18. Shopping Discount

A customer gets a discount if:

* their purchase amount is **₹5000 or more**
* OR they are a **premium member**

Take:

* purchase amount
* premium membership status

from the user.

Print:

```text
Discount Available: True/False
```

---

### Q19. Tricky Boolean Expression

Without running the code first, predict the output of each:

```python
print(10 > 5 and 20 > 15)
print(10 > 5 and 20 < 15)
print(10 > 5 or 20 < 15)
print(not 10 > 5)
print(not (10 > 5 and 20 > 15))
```

Then run the code and verify your answers.

---

### Q20. 🔥 Final Challenge — Student Eligibility System

Create a small **Student Eligibility System**.

Take these inputs:

* age
* percentage
* attendance percentage
* has_backlog (`True`/`False`)
* entrance_exam_passed (`True`/`False`)

A student is eligible if:

1. Age is **17 or above**
2. Percentage is **60 or above**
3. Attendance is **75 or above**
4. Student has **no backlog**
5. Entrance exam is passed

Create Boolean expressions for each condition and then combine them into one final variable:

```python
is_eligible
```

Your output should look something like:

```text
Age Eligible: True
Percentage Eligible: True
Attendance Eligible: False
No Backlog: True
Entrance Exam Passed: True

Final Eligibility: False
```

---

## 🎯 Bonus Challenge

Try to solve these without creating unnecessary `if-else` statements.

Focus on understanding how:

```python
>
<
>=
<=
==
!=
and
or
not
```

produce `True` or `False`.

### Submission

Solve **Q1 → Q20** in one Python file:

```text
boolean-assessment.py
```

Then send me your code.

I will evaluate it **question by question**, give you a **score out of 10**, identify logic mistakes, and suggest **industry-relevant improvements without simply rewriting your code for you**.