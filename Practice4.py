# Practice 1
def DOB():
    day = 0
    question1 = "Is your birthday in Set1?\n" + \
    " 1 3 5 7\n" + \
    " 9 11 13 15\n" + \
    "17 19 21 23\n" + \
    "25 27 29 31" + \
    "\nEnter 0 for No and 1 for Yes: "
    answer = eval(input(question1))

    if answer == 1 :
        day += 1

    question2 = "Is your birthday in Set2?\n" + \
    " 2 3 6 7\n" + \
    "10 11 14 15\n" + \
    "18 19 22 23\n" + \
    "26 27 30 31" + \
    "\nEnter 0 for No and 1 for Yes: "
    answer = eval(input(question2))

    if answer == 1 :
        day += 2

    question3 = "Is your birthday in Set3?\n" + \
    " 4 5 6 7\n" + \
    "12 13 14 15\n" + \
    "20 21 22 23\n" + \
    "28 29 30 31" + \
    "\nEnter 0 for No and 1 for Yes: "
    answer = eval(input(question3))
    if answer == 1 :
        day += 4

    question4 = "Is your birthday in Set4?\n" + \
    " 8 9 10 11\n" + \
    "12 13 14 15\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31" + \
    "\nEnter 0 for No and 1 for Yes: "
    answer = eval(input(question4))

    if answer == 1:
     day += 8

    # Prompt the user to answer the fifth question
    question5 = "Is your birthday in Set5?\n" + \
    "16 17 18 19\n"+ \
    "20 21 22 23\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31" + \
    "\nEnter 0 for No and 1 for Yes: "
    answer = eval(input(question5))

    if answer == 1:
        day += 16
        print("\nYour birthday is "+ str(day) + "!")    


#     ---------------------------------------------------


# Practice 2


year = eval(input("Enter a year: "))
zodiacYear = year % 12
if zodiacYear == 0:
 print("monkey")
elif zodiacYear == 1:
 print("rooster")
elif zodiacYear == 2:
 print("dog")
elif zodiacYear == 3:
 print("pig")
elif zodiacYear == 4:
 print("rat")
elif zodiacYear == 5:
 print("ox")
elif zodiacYear == 6:
 print("tiger")
elif zodiacYear == 7:
 print("rabbit")
elif zodiacYear == 8:
 print("dragon")
elif zodiacYear == 9:
 print("snake")
elif zodiacYear == 10:
 print("horse")
else:
 print("sheep")

#     ---------------------------------------------------


# Practice 3

# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

# Prompt the user to enter height in inches
height = eval(input("Enter height in inches: "))

KILOGRAMS_PER_POUND = 0.45359237 
METERS_PER_INCH = 0.0254 

weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
 print("Underweight")
elif bmi < 25:
 print("Normal")
elif bmi < 30:
 print("Overweight")
else:
 print("Obese")

#     ---------------------------------------------------

# Practice 4

import sys

status = eval(input(
    "(0-single filer, 1-married jointly,\n" +
    "2-married separately, 3-head of household)\n" +
    "Enter the filing status: "))

income = eval(input("Enter the taxable income: "))
tax = 0

if status == 0: 
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
        (income - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
        (372950 - 171550) * 0.33 + (income - 372950) * 0.35;
elif status == 1: 
    print("Left as exercise")
elif status == 2: 
    print("Left as exercise")
elif status == 3: 
    print("Left as exercise")
else:
    print("Error: invalid status")
    sys.exit()
print("Tax is", format(tax, ".2f"))


#     ---------------------------------------------------

# Algebra Quaderetic equation Excercise 4.1
import math
def quaderic_eqation():
    a=eval(input("Enter the value of a: "))
    b=eval(input("Enter the value of b: "))
    c=eval(input("Enter the value of c: "))

    discriminant=b**2-4*a*c

    root1_upper= -b + math.sqrt(discriminant)
    root1_lower=2*a
    root1_total=root1_upper/root1_lower

    root2_upper=- b -math.sqrt(discriminant)
    root2_lower=2*a
    root2_total=root2_upper/root2_lower

    if discriminant==0:
        print(root2_total)
    elif discriminant !=0:
        print("The roots are",root2_total,"and",root1_total)
    else:
        print("The equation has no real roots")


#     ---------------------------------------------------

# Algebra random number Excercise 4.2

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)

answer = eval(input("What is "+ str(number1) + " + "+ str(number2) + "? "))
answer2 = eval(input("What is "+ str(number1) + " + "+ str(number2)+ " + "+ str(number3)  +  "? "))

if answer == True:
    print(number1, "+", number2, "=", answer,"is", number1 + number2 == answer)
else:
    print(number1, "+", number2, "+", number3, "=" ,answer,"is", number1 + number2 + number3 == answer2)


#     ---------------------------------------------------


# Algebra 2 X 2 linear equation Excercise 4.3
def linear_equation():
    a=eval(input("Enter the value of a: "))
    b=eval(input("Enter the value of b: "))
    c=eval(input("Enter the value of c: "))
    d=eval(input("Enter the value of d: "))
    e=eval(input("Enter the value of e: "))
    f=eval(input("Enter the value of f: "))

    no_solution=a*d-b*c

    x_upper=e*d-b*f
    x_total=x_upper/no_solution

    y_upper=a*f-e*c
    y_total=y_upper/no_solution
    if no_solution == 0:
        print("The equation has no solution")
    else:
        print("x is",x_total ,"and y is", y_total)

#     ---------------------------------------------------


# Algebra 2 X 2 linear equation Excercise 4.4
import random

number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

answer = eval(input("What is "+ str(number1) + " + "+ str(number2) + "? "))
if answer == answer:
    print("True")
else:
    print("False")

#     ---------------------------------------------------


# day after three days Excercise 4.5

import datetime

x = datetime.datetime()

print(x.strftime("%A"))


#     ---------------------------------------------------


# day after three days Excercise 4.6

# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

# Prompt the user to enter height in inches
height = eval(input("Enter height in inches: "))

KILOGRAMS_PER_POUND = 0.45359237 
METERS_PER_INCH = 0.0254 

weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
 print("Underweight")
elif bmi < 25:
 print("Normal")
elif bmi < 30:
 print("Overweight")
else:
 print("Obese")

#     ---------------------------------------------------


# day after three days Excercise 4.8
print("Input Three integers:")
nums = list(map(int, input().split()))
nums.sort()
print("After sorting the said ntegers:")
print(*nums)


#     ---------------------------------------------------


# day after three days Excercise 4.11


month = int (input ('month (1-12): '))

if month < 13:
    if month == 2:
        year = int (input ('year: '))
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print ('29')
                else:
                    print ('28')
            else:
                print ('29')
        else:
            print ('28')

    elif month >= 8:
        if month % 2 == 0:
            print ('31')
        else:
            print ('30')

    elif month % 2 == 0:
        print ('30')
    else:
        print ('31')

else:
    print ('Only 1-12 accepted')
  
#     ---------------------------------------------------


# day after three days Excercise 4.12

number = int(input(" Please Enter any Positive Integer : "))

if((number % 5 == 0) and (number % 6 == 0)):
    if number == True:
        print("True")
    else:
        print("False")
else:
    print("Is 10 divisible by 5 or 6, but not both")


#     ---------------------------------------------------


# day after three days Excercise 4.13



from random import random

def heads_or_tails():
    guess = input('Pick heads or tails and then press eneter to play: ')
    if random() > 0.5:
        return 'tails'
    else:
        return 'heads'

print(heads_or_tails() + ' wins' + '!')


#     ---------------------------------------------------


# day after three days Excercise 4.13

import random
import time

##Declare Variables
user_num=0
##lottery_num=random.randint(10,99)
lottery_num=12

##Input
print("Welcome to the Lottery Program!")
user_num=int(input("Please enter a two digit number: "))
print("Calculating Results.")
for i in range(3):
  time.sleep(1)
  print(".")

##Calc & Output
lottery_tens = lottery_num // 10
lottery_ones = lottery_num % 10

user_tens = user_num // 10
user_ones = user_num % 10
if lottery_num == user_num:
    print("All your numbers match in exact order! Your reward is $10,000!\n")
elif lottery_tens == user_ones and lottery_ones == user_tens:
    print("All your numbers match! Your reward is $3,000!\n")
elif lottery_tens == user_tens or lottery_ones == user_ones \
  or lottery_ones == user_tens or lottery_tens == user_ones:
    print("One of your numbers match the lottery. Your reward is $1,000!\n")
else:
    print("Your numbers don't match! Sorry!")


#     ---------------------------------------------------


# day after three days Excercise 4.14
  
test_str = input("Enter a Word: ")
res =str.upper(test_str)
  
print("Random Uppercased Strings : " + str(res))

#     ---------------------------------------------------


# day after three days Excercise 4.15

import random
  
# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
  
while True:
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
      
    # take the input from user
    choice = int(input("User turn: "))
  
    # OR is the short-circuit operator
    # if any one of the condition is true
    # then it return True value
      
    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
          
    # print user choice 
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")
  
    # Computer chooses randomly any number 
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)
      
    # looping until comp_choice value 
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
  
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
          
    print("Computer choice is: " + comp_choice_name)
  
    print(choice_name + " V/s " + comp_choice_name)
  
    # condition for winning
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("paper wins => ", end = "")
        result = "paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
    else:
        print("scissor wins =>", end = "")
        result = "scissor"
  
    # Printing either user or computer wins
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
          
    print("Do you want to play again? (Y/N)")
    ans = input()
  
  
    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break
      
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")


#     ---------------------------------------------------


# day after three days Excercise 4.16

import requests


SUPPORTED_CURRENCIES = {
    "EUR": "European euro",
    "USD": "US dollar",
    "GBP": "Pound sterling",
    "BRL": "Brazilian real"
}


CURRENCY_CODES = {
    1: "EUR",
    2: "USD",
    3: "GBP",
    4: "BRL"
}


def get_exchange_rate(base_currency, target_currency):
    if not (base_currency in SUPPORTED_CURRENCIES.keys()):
        raise ValueError("base currency {} not supported".format(base_currency))
    if not (target_currency in SUPPORTED_CURRENCIES.keys()):
        raise ValueError("target currency {} not supported".format(target_currency))

    if base_currency == target_currency:
        return 1

    api_uri = "https://api.fixer.io/latest?base={}&symbols={}".format(base_currency, target_currency)
    api_response = requests.get(api_uri)

    if api_response.status_code == 200:
        return api_response.json()["rates"][target_currency]


if __name__ == '__main__':
    print("Welcome to Currency Converter")

    amount = float(input("Enter the amount you wish to convert: "))

    print("Choose a base currency among our supported currencies:")
    while True:
        for code, currency in CURRENCY_CODES.items():
            print("code {}: base {}".format(code, currency))
        base_currency_code = int(input("Please digit the code: "))
        if base_currency_code in CURRENCY_CODES.keys():
            break
        else:
            print("Invalid code")
    base_currency = CURRENCY_CODES[base_currency_code]

    print("Choose a target currency among our supported currencies:")
    while True:
        for code, currency in CURRENCY_CODES.items():
            print("code {}: target {}".format(code, currency))
        target_currency_code = int(input("Please digit the code: "))
        if target_currency_code in CURRENCY_CODES.keys():
            break
        else:
            print("Invalid code")
    target_currency = CURRENCY_CODES[target_currency_code]

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    print("{} {} is {} {}".format(amount, base_currency, amount * exchange_rate, target_currency))


#     ---------------------------------------------------


# day after three days Excercise 4.16

import random
cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    return(f"The {rank} of {card}")

print(pick_a_card())

#     ---------------------------------------------------


# day after three days Excercise 4.26

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

#     ---------------------------------------------------


# day after three days Excercise 4.27

def convert24(str1):
    
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
 
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]
  
print(convert24("08:05:45 PM"))

#     ---------------------------------------------------


# day after three days Excercise 4.26

decimal = int(input("Enter the Decimal no that you want to convert to Hexadecimal : "))
intact = decimal
hexadecimal = ''
dictionary = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

while(decimal!=0):
    c = decimal%16 
    hexadecimal =  dictionary[c] + hexadecimal 
    decimal = int(decimal/16)

print(f"{intact} is {hexadecimal} in Hexadecimal")


#     ---------------------------------------------------


# day after three days Excercise 4.33


test_string = 'A'
  
# printing original string 
print("The original stringg : " + str(test_string))
  
# using int()
# converting hexadecimal string to decimal
res = int(test_string, 16)
  
# print result
print("The decimal number of hexadecimal string : " + str(res))