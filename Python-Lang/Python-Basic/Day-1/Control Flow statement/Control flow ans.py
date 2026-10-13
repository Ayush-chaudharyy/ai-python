# # QUESTION-1
# num = int(input('Enter a number:-'))
# if num > 0:
#     print('Positive number')
# else:
#     print('Negative number')


# # QUESTION-2
# age = int(input('Enter a age:-'))
# if age >= 18:
#     print('You are eligible to vote')



# # QUESTION-3
# num = int(input('Enter a number:-'))
# if num % 2 == 0:
#     print('Even number.')


# # QUESTION-4
# num = int(input('Enter a number:-'))
# if num % 5 == 0:
#     print('Number is divisible by 5')


# # QUESTION-5
# string = input('Enter a string:')
# if len(string) > 10:
#     print('Long string')


# # QUESTION-6
# num = int(input('Enter a number:-'))
# if num >= 0:
#     print('Positive number')
# else:
#     print('Negative number')

# # QUESTION-7
# num = int(input('Enter a number:-'))
# if num % 2 == 0:
#     print('Even number.')
# else:
#     print('Odd number.')



# # QUESTION-8
# marks = float(input('Enter a marks:-'))
# if marks >= 40:
#     print('Pass')
# else:
#     print('Fail')



# # QUESTION-9
# correct_username = "admin"
# correct_password = "1234"

# username =input('Enter your username:-')
# password =input('Enter your password:-')

# if username == correct_username and password == correct_password:
#     print('Login Successfully.')
# else:
#     print('Invalid username or password.')


# # QUESTION-10
# num1 = int(input('Enter a number:-'))
# num2 = int(input('Enter a number:-'))
# if num1 > num2:
#     print('First number is greater.')
# else:
#     print('Second number is greater.')

# # QUESTION-11
# num = int(input('Enter a number:-'))
# if num > 0:
#     print('Positive')
# elif num < 0:
#     print('Negative')
# else:
#     print('Zero')

# # QUESTION-12
# marks = float(input('Enter a marks:-'))
# if marks <= 100 and marks >= 90:
#     print('A')
# elif marks <= 89 and marks >= 80:
#     print('B')
# elif marks <= 79 and marks >= 70:
#     print('C')
# elif marks <= 69 and marks >= 60:
#     print('D')
# else:
#     print('F')


# # QUESTION-13
# temp = float(input('Enter a temperature in celcious:-'))
# if temp < 10:
#     print('Cold')
# elif temp >= 10 and temp <=24:
#     print('Cool')
# elif temp >= 25 and temp <=34:
#     print('Warm')
# elif temp >= 35:
#     print('Hot')


# # QUESTION-14
# num = int(input('Enter a number from 1 to 7:-'))
# if num == 1:
#     print('Monday')
# elif num == 2:
#     print('Tuesday')
# elif num == 3:
#     print('Wednesday')
# elif num == 4:
#     print('Thuersday')
# elif num == 5:
#     print('Friday')
# elif num == 6:
#     print('Saturday')
# elif num == 7:
#     print('Sunday')


# # QUESTION-15
# num_1 = int(input('Enter a number:-'))
# num_2 = int(input('Enter a number:-'))
# operator = input('Enter a operator:-')
# if operator == "+":
#     print(num_1 + num_2)
# elif operator == "-": 
#     print(num_1 - num_2)
# elif operator == "*":
#     print(num_1 * num_2)
# elif operator == "/":
#     print(num_1 / num_2)
# else:
#     print('Invalid operator')


# # QUESTION-16
# age = int(input('Entere your age:-'))
# if age < 5 :
#     print('Free')
# elif age <= 12 and age >5:
#     print('Rs 100')
# elif age <= 59 and age >13:
#     print('Rs 200')
# elif age >= 60:
#     print('Rs 120')


# # QUESTION-17
# electr_unit = int(input('Enter a electricity unit:-'))
# if electr_unit < 100:
#     print('Total bill amount:-',electr_unit * 5)
# elif electr_unit < 200:
#     print('Total bill amount:-',electr_unit * 7)
# elif electr_unit < 300:
#     print('Total bill amount:-',electr_unit * 10)
# else:
#     print('Total bill amount:-',electr_unit * 12)


# # QUESTION-18
# python_marks = float(input('Enter a marks:-'))
# sql_marks = float(input('Enter a marks:-'))
# math_marks = float(input('Enter a marks:-'))
# avg_marks = (python_marks + sql_marks + math_marks)/3
# if avg_marks >= 90:
#     print('A')
# elif avg_marks >= 75:
#     print('B')
# elif avg_marks >= 60:
#     print('C')
# else:
#     print('D')


# # QUESTION-19
# account_bal = int(input('Enter a account balance:-'))
# withdraw_amount = int(input('Enter a widraw  amount:-'))
# if withdraw_amount <= 0:
#     print('Invalid amount')
# elif withdraw_amount > account_bal:
#     print('Insufficient balance')
# else:
#     print('Withdraw successfully')
# remain = account_bal - withdraw_amount
# print("Remaining balance:",remain)

# QUESTION-20
age = int(input('Enter a age:-'))
percentage = float(input('Enter a percentage:-'))
atten_per = int(input('Enter a attendence percentage:-'))
back_status = input('Enter a backlog status Yes/N0:-').lower()
enterence_status = input('Enter a Enterance exam status Yes/N0:-').lower()
if age < 17:
    print('Not eligible: Age requirement not met')
elif percentage < 60:
    print("Not eligible: Percentage requirement not met")
elif atten_per < 75:
    print("Not eligible: Attendance requirement not met")
elif back_status == 'yes':
    print("Not eligible: Backlog detected")
elif enterence_status == 'no':
    print('Not eligible: Entrance exam not cleared')
else:
    print('Congratulations! You are eligible.')
    