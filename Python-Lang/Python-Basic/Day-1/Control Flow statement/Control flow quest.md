# 🐍 Python Conditionals — Assessment

## Topic

`if` • `elif` • `else`

**Total Questions:** 20


---

# 🟢 PART A — `if`

## Q1–Q5

### Q1. Positive Number

Take an integer from the user.

If the number is greater than `0`, print:

```text
Positive number
```

If the number is `0` or negative, don't print anything.

---

### Q2. Age Check

Take the user's age.

If the age is **18 or above**, print:

```text
You are eligible to vote.
```

Don't print anything if the age is below 18.

---

### Q3. Even Number

Take an integer from the user.

If the number is even, print:

```text
Even number
```

Use the modulo operator `%`.

---

### Q4. Divisible by 5

Take a number from the user.

If the number is completely divisible by `5`, print:

```text
Number is divisible by 5
```

---

### Q5. String Length

Take a string from the user.

If the string contains **more than 10 characters**, print:

```text
Long string
```

Otherwise, don't print anything.

---

# 🟡 PART B — `if-else`

## Q6–Q10

### Q6. Positive or Negative

Take an integer from the user.

Print:

```text
Positive
```

if the number is greater than or equal to `0`.

Otherwise print:

```text
Negative
```

---

### Q7. Even or Odd

Take an integer from the user.

Use `if-else` to determine whether the number is:

```text
Even
```

or

```text
Odd
```

---

### Q8. Pass or Fail

Take marks from the user.

A student passes if marks are **40 or above**.

Print:

```text
Pass
```

or:

```text
Fail
```

---

### Q9. Login Check

Create:

```python
correct_username = "admin"
correct_password = "1234"
```

Take username and password from the user.

If both are correct, print:

```text
Login successful
```

Otherwise:

```text
Invalid username or password
```

---

### Q10. Greater Number

Take two numbers from the user.

Print:

* `"First number is greater"` if the first number is greater
* `"Second number is greater"` otherwise

Test your program with different values.

---

# 🟠 PART C — `if-elif-else`

## Q11–Q15

### Q11. Number Classification

Take a number from the user.

Print:

* `"Positive"` if greater than `0`
* `"Negative"` if less than `0`
* `"Zero"` if equal to `0`

Use `if-elif-else`.

---

### Q12. Grade Calculator

Take marks from the user.

Assign grades using:

|    Marks | Grade |
| -------: | :---- |
|   90–100 | A     |
|    80–89 | B     |
|    70–79 | C     |
|    60–69 | D     |
| Below 60 | F     |

Print the appropriate grade.

---

### Q13. Temperature Classification

Take temperature in Celsius.

Print:

* Below `10` → `"Cold"`
* `10–24` → `"Cool"`
* `25–34` → `"Warm"`
* `35` or above → `"Hot"`

Use `if-elif-else`.

---

### Q14. Day Number

Take a number from `1` to `7`.

Print:

```text
1 → Monday
2 → Tuesday
3 → Wednesday
4 → Thursday
5 → Friday
6 → Saturday
7 → Sunday
```

If the user enters anything outside `1–7`, print:

```text
Invalid day
```

---

### Q15. Simple Calculator

Take:

* First number
* Second number
* Operator (`+`, `-`, `*`, `/`)

Use `if-elif-else` to perform the requested operation.

Example:

```text
Enter first number: 20
Enter second number: 5
Enter operator: *

Result: 100
```

Handle an invalid operator with:

```text
Invalid operator
```

Also handle division by zero appropriately.

---

# 🔴 PART D — Practical Conditional Problems

## Q16–Q20

### Q16. Movie Ticket Price

Take the user's age.

Ticket pricing:

* Age below 5 → Free
* Age 5–12 → ₹100
* Age 13–59 → ₹200
* Age 60 or above → ₹120

Print the applicable ticket price.

---

### Q17. Electricity Bill

Take electricity units consumed.

Calculate the bill using:

|     Units |     Rate |
| --------: | -------: |
|     0–100 |  ₹5/unit |
|   101–200 |  ₹7/unit |
|   201–300 | ₹10/unit |
| Above 300 | ₹12/unit |

Print:

```text
Units consumed: ...
Total bill: ₹...
```

**Important:** Use the slabs exactly as specified in the question.

---

### Q18. Student Result System

Take marks for three subjects:

* Python
* SQL
* Mathematics

Calculate the average.

Rules:

* If **any subject is below 40** → `"Fail"`
* Otherwise:

  * Average ≥ 90 → `"A Grade"`
  * Average ≥ 75 → `"B Grade"`
  * Average ≥ 60 → `"C Grade"`
  * Average ≥ 40 → `"D Grade"`

Print:

```text
Total Marks: ...
Average: ...
Result: ...
```

This question tests **Boolean conditions + `if-elif-else`**.

---

### Q19. ATM Withdrawal

Take:

* Account balance
* Withdrawal amount

Rules:

1. If withdrawal amount is less than or equal to `0` → `"Invalid amount"`
2. If withdrawal amount is greater than balance → `"Insufficient balance"`
3. Otherwise → perform the withdrawal and print the remaining balance.

Example:

```text
Balance: ₹10000
Withdrawal: ₹3000

Withdrawal successful
Remaining balance: ₹7000
```

---

### Q20. 🔥 Final Challenge — Student Eligibility System

Create a **Student Eligibility System**.

Take the following from the user:

* Age
* Percentage
* Attendance percentage
* Backlog status (`yes/no`)
* Entrance exam status (`yes/no`)

Determine eligibility using these rules:

### Step 1 — Age

If age is below `17`:

```text
Not eligible: Age requirement not met
```

### Step 2 — Percentage

If age is valid but percentage is below `60`:

```text
Not eligible: Percentage requirement not met
```

### Step 3 — Attendance

If age and percentage are valid but attendance is below `75`:

```text
Not eligible: Attendance requirement not met
```

### Step 4 — Backlog

If the student has a backlog:

```text
Not eligible: Backlog detected
```

### Step 5 — Entrance Exam

If all previous conditions are satisfied but the entrance exam wasn't passed:

```text
Not eligible: Entrance exam not cleared
```

### Final Result

If every condition is satisfied:

```text
Congratulations! You are eligible.
```

Use a proper `if-elif-else` structure.

---

# 🎯 Concepts You Should Master

By the end of these 20 questions, you should understand:

### Basic

```python
if condition:
    # code
```

### Two possibilities

```python
if condition:
    # code
else:
    # code
```

### Multiple possibilities

```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

### Conditions with comparison operators

```python
>
<
>=
<=
==
!=
```

### Combining conditions

```python
and
or
not
```

### Useful operators for your problems

```python
%
```

and Boolean expressions such as:

```python
age >= 18
marks >= 40
number % 2 == 0
username == correct_username
```

---------------------------------END---------------------------------------------------------