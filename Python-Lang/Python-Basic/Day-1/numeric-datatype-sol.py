# QUESTION-1
a = 25
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# QUESTION - 2
a = int(input('Enter a number:-'))
b = int(input('Enter a number:-'))
print('Addittion:-',a + b)
print('Substraction:-',a - b)
print('Multiplication:-',a * b)
print('Floor division:-',a // b)
print('Reminder:-',a % b)


# QUESTION-3
num = int(input('Enter a number:-'))
print(num * 2)
print(num * 3)
print(num * 5)
print(num ** 2)

# QUESTION-4
x = 50
x += 25
print(x)

x -= 10
print(x)

x *= 2
print(x)

x //= 5
print(x)


# QUESTION-5
a = int(input('Enter a two digit intiger:-'))
tens = a // 10
once = a % 10
print('Tense value is',tens)
print('once value is',once)


# QUESTION-6
a = int(input('Enter a two digit intiger:-'))
tens = a // 10
once = a % 10

print(f'reverse is {once}{tens}')


# QUESTION-7
a = int(input('Enter a three digit intiger:-'))
hundred = a // 100
tens = (a % 100) // 10
once = (a % 100) % 10 
print(hundred)
print(tens)
print(once)

# QUESTION-8
a = int(input('Enter a three digit value'))
hundred = a // 100
tens = (a % 100) // 10
once = (a % 100) % 10 
sum = hundred + tens + once
print(sum)

# QUESTION-9
a = int(input('Enter a value:-'))
last_digi = a % 10
print(last_digi)




# QUESTION-11
total_seco = int(input('Enter a total second'))
hour = total_seco // 3600
rem_sec = total_seco % 3600

min = rem_sec // 60
second = rem_sec % 60
print(f'hours:-{hour},minutes:-{min},second:-{second}')

# QUESTION-12
age = int(input('Enter a age:-'))
total_days = age * 365
print('Days lived is :',total_days)

# QUESTION-13
principal = float(input('Enter a principle amount:'))
rate = float(input('Enter a rate:'))
time = float(input('Enter a time:'))

sim_int =(principal * rate * time) / 100
amount = principal + sim_int
print(sim_int)
print(amount)

# QUESTION-14
x = int(input('Enter a intiger:'))
result = 3*x**2 + 5*x + 10
print(result)

# QUESTION-15
x = 10
x += 20
print(x)
x -= 3
print(x)
x //= 5
print(x)
x %= 4
print(x)

# QUESTION-16
a = 12.5
b = 2.5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)


# QUESTION-17
a = float(input('Enter a number:-'))
b = float(input('Enter a number:-'))
print('Addittion:-',a + b)
print('Substraction:-',a - b)
print('Multiplication:-',a * b)
print('Floor division:-',a / b)
print('Reminder:-',a % b)

# QUESTION -18
a = float(input('Enter a number:'))
b = float(input('Enter a number:'))
c = float(input('Enter a number:'))

total = a + b + c
avg = total / 3
print(total)
print(avg)

# Q19. Temperature Conversion

celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)


# Q20. Rectangle with Decimal Values

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)


# Q21. Circle Area

radius = float(input("Enter radius: "))
pi = 3.14159

area = pi * radius ** 2

print("Area:", area)


# Q22. Circle Circumference

radius = float(input("Enter radius: "))
pi = 3.14159

circumference = 2 * pi * radius

print("Circumference:", circumference)


# Q23. Simple Interest with Decimal Values

P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
T = float(input("Enter time: "))

SI = (P * R * T) / 100

print("Simple Interest:", SI)


# Q24. Profit Percentage

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

profit = selling_price - cost_price
profit_percentage = (profit / cost_price) * 100

print("Profit:", profit)
print("Profit Percentage:", profit_percentage)


# Q25. Discount Calculator

price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)


# Q26. GST Calculator

price = float(input("Enter product price: "))
gst = float(input("Enter GST percentage: "))

gst_amount = price * gst / 100
final_price = price + gst_amount

print("GST Amount:", gst_amount)
print("Final Price:", final_price)


# Q27. BMI Calculator

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / height ** 2

print("BMI:", bmi)


# Q28. Speed Calculator

distance = float(input("Enter distance in km: "))
time = float(input("Enter time in hours: "))

speed = distance / time

print("Speed:", speed, "km/h")


# Q29. Multi-Step Price Calculation

price = 2500.50
discount = 12.5
gst = 18

discount_amount = price * discount / 100
price_after_discount = price - discount_amount

gst_amount = price_after_discount * gst / 100
final_price = price_after_discount + gst_amount

print("Original Price:", price)
print("Discount Amount:", discount_amount)
print("Price After Discount:", price_after_discount)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)


# Q30. Final Numeric Data Type Challenge

name = input("Enter student name: ")

python_marks = float(input("Enter Python marks: "))
sql_marks = float(input("Enter SQL marks: "))
math_marks = float(input("Enter Mathematics marks: "))

total = python_marks + sql_marks + math_marks
average = total / 3
percentage = (total / 300) * 100

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage)

