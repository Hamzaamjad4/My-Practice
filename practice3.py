# Function to find character ASCII code Excercise 3.6
def ASCII():
    c=eval(input("Enter a ASCII code: "))
    print("The character is",chr(c))

#     --------------------------------------------------


# Function to find character ASCII code Excercise 3.7

import time

def random():
    n1 =int(time.time()) % 25+65
    n2 =int(time.time())% 25+97
    print(chr(n1)," ",chr(n2))


#     --------------------------------------------------


# Function to find character ASCII code Excercise 3.9

def pay():
    name=input("Enter employee's name: ")
    hours=eval(input("Enter number of hours worked in a week: "))
    payrate=eval(input("Enter hourly pay rate: "))
    federal_tax=eval(input("Enter federal tax withholding rate: "))
    state_tax=eval(input("Enter state tax withholding rate: "))

    total_pay_in_week= payrate*hours
    federal_tax_minus=total_pay_in_week/100*federal_tax    
    state_tax_minus=total_pay_in_week/100*state_tax
    total_deduction=federal_tax_minus+state_tax_minus
    total_pay=total_pay_in_week-total_deduction
    print("Employee name: ",name)
    print("Hours Worked: ",hours)
    print("Pay Rate: ",payrate)
    print("Gross Pay: ",total_pay_in_week)
    print("Deductions: \n Federal Withholding (20.0%): ",federal_tax_minus)
    print(" State Withholding (9.0%): ",state_tax_minus)
    print(" Total Deduction: ",total_deduction)
    print("Net Total: ",total_pay)




#     --------------------------------------------------


# Function to find character ASCII code Excercise 3.10

def greeks():  
    print('\u03b1','\u03b2' ,'\u03b3 ','\u03b4 ','\u03b5','\u03b6','\u03b7',' \u03b8')



#     --------------------------------------------------


# Function to find character ASCII code Excercise 3.11

def reverse():
    number1 = int(input("Enter the integer number: "))  
    number2 = int(input("Enter the integer number: "))  
    number3 = int(input("Enter the integer number: "))
    number4 = int(input("Enter the integer number: "))  

    print(number4)
    print(number3)
    print(number2)
    print(number1)
