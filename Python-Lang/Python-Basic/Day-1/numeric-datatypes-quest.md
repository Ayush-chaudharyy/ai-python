# Python Practice Lab: Numeric Data Types, Arithmetic & Math Functions

---

# Phase 1: Medium (Questions 1–10)
Focus: Operations, operator precedence, built-in functions, and basic assignments.

# Question 1: Floor Division vs Float Division
Write code to calculate both 17 / 4 and 17 // 4. Print the outputs along with their respective Python data types using type().

# Question 2: Modulo Mechanics
Calculate 23 % 5 and -23 % 5. Explain in a comment why Python handles the negative modulo result the way it does.

# Question 3: Exponentiation Precedence
Evaluate the difference between -3 ** 2 and (-3) ** 2 using code. Print both and explain the precedence rule causing the difference.

# Question 4: Rounding Precision
Use the built-in round() function on the float 12.5567 to round it to:
* 0 decimal places
* 2 decimal places
* -1 decimal places(rounding to the nearest 10)

# Question 5: Absolute Difference
Given two numbers a = 14.8 and b = 29.3, calculate their absolute difference using abs() without caring which variable is larger.

# Question 6: Compound Assignment Sequences
Start with a variable x = 10. Perform the following operations sequentially using compound assignment operators(` += `, ` -= `, ` *= `, ` /= `, ` //= `):
* Add 5
* Multiply by 2
* Subtract 4
* Floor divide by 3
* Print the final value and data type of x.

# Question 7: Type Coercion in Arithmetic
What happens to the data type when you perform 10 + 5.0 versus 10 + 5? Write code to demonstrate the automatic type promotion.

# Question 8: Comparison Chaining
Create a variable score = 85. Write a single chained comparison expression(e.g., a < b < c) that checks if score is strictly between 70 and 100.

# Question 9: Built-in Min/Max
Given the numbers -15, 0, 42, -8, 19, write a single line of code using min() and max() to find the sum of the smallest and largest values.

# Question 10: Complex Number Extraction
Create a complex number z = 4 + 7j. Extract and print its real part, imaginary part, and calculate its conjugate using .conjugate().

---

# Phase 2: Upper-Medium (Questions 11–20)
Focus: Importing math, precision issues, trigonometry, powers, and tricky comparisons.

# Question 11: Square Root vs Power
Import the math module. Calculate the square root of 144 using math.sqrt() and using the exponentiation operator ** 0.5. Check if their types and values are identical using ` == ` and ` is `.

# Question 12: Ceil vs Floor
Given x = -4.3 and y = 4.3, apply math.ceil() and math.floor() to both. Print all four outputs.

# Question 13: Factorials and GCD
Using the math module, calculate the factorial of 7 and find the Greatest Common Divisor(GCD) between 84 and 120.

# Question 14: Logarithmic Calculations
Calculate the natural log(base e) of 100 and the log base 10 of 1000 using math.log() and math.log10().

# Question 15: Floating Point Imprecision
Evaluate 0.1 + 0.2 == 0.3 in Python. Print the result. Then, use math.isclose() to perform a safe comparison between 0.1 + 0.2 and 0.3.

# Question 16: Hypotenuse Calculation
Given two sides of a right triangle a = 6 and b = 8, calculate the hypotenuse c using math.hypot(a, b). Verify it manually using the Pythagorean theorem.

# Question 17: Trigonometric Conversion
Calculate the sine of 45°. (Hint: Python's math.sin() expects radians. Convert 45° to radians first using math.radians()).

### Question 18: Bitwise-Style Assignment on Ints
Initialize flags = 8. Use *= to double it, then //= to halve it, and finally **= to square it. Print the final result.

### Question 19: Comparing Mixed Types
Evaluate True == 1, False == 0, and True + True + False. Print all three results and explain why Python permits arithmetic on booleans.

### Question 20: Truncation vs Floor
Compare math.trunc(-3.7) with math.floor(-3.7). Print both outputs and explain the structural differe…