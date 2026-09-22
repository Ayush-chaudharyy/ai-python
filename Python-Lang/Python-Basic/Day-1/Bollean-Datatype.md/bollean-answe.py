# # QUESTION-1
# is_student = True
# has_job = False
# print(is_student)
# print(has_job)
# print("Type is:",type(is_student))
# print("Type is:",type(has_job))

# # QUESTION-2
# value1 = int(input('Enter a 0:'))
# value2 = int(input('Enter a 1:'))
# value3 = input('Enter a empty string:')
# value4 = input('Enter a non empty string:')
# print(bool(value1))
# print(bool(value2))
# print(bool(value3))
# print(bool(value4))



# # QUESTION-3
# a = 25
# b = 40
# print("a is grater then b :",a > b)
# print("a is less then b :",a < b)
# print("a is equal to b :",a == b)

# # QUESTION-4
# num1 = int(input('Enter a number:'))
# num2 = int(input('Enter a number:'))
# print(num1 == num2)
# print(num1 != num2)

# # QUESSTION-5
# a = int(input('Enter a number:-'))
# is_even = (a % 2 == 0)
# print('Is even:',is_even)

# # QUESTION-6
# age = int(input('Enter a age:'))
# is_adult = (age>18)
# print(is_adult)

# # QUESTION-7
# mark = int(input('Enter a marks:-'))
# stu_pass = (mark >= 40)
# print('Passed:-',stu_pass)



# # QUESTION-8
# a = int(input('Enter a number:-'))
# print(a >= 10 and a<= 50 )


# # QUESTION-9
# num1 = int(input('Enter a number:-'))
# num2 = int(input('Enter a number:-'))
# fir_grater = num1 > num2
# sec_grater = num2 > num1
# equal = num1 == num2
# print('first number grater:',fir_grater)
# print('second number grater:',sec_grater)
# print('are they equal:',equal)


# # QUESTION-10
# a = float(input('Take the current temperature:-'))
# print('below 10c:',a < 10)
# print('between 10c and 30c:', a>10 and a<30)
# print('above 30c:',a > 30)

# # QUESTION-11
# age = int(input('Enter a age:-'))
# has_id = True
# print('Person is Eligility',age >= 18 and has_id)


# QUESTION-12
has_student_id = True
has_registration_number = False

is_eligible = has_student_id or has_registration_number

print("Competition Eligible:", is_eligible)

