# 3.1

import math
# number = eval(input("Enter the integer number: ")) 
# a = math.pi / 5
# radius=2*number*math.sin(a)

# area=3* math.sqrt(3)/2*radius**2
# print(area)

def circle_radius():
    x1 = eval(input("Enter x1: "))
    x2 = eval(input("Enter x2: "))
    y1 = eval(input("Enter y1: "))
    y2 = eval(input("Enter y2: "))

    radius=6371.01*math.cos(math.sin(x1)*math.sin(x2))
    radius2=math.cos(x1)*math.cos(x2)*math.cos(y1+y2)
    total_radius=radius+radius2
    print(total_radius)

# def pentagon():
#     s = eval(input("Enter x1: "))
#     Area_half = 5*s**2
#     area_second_half=4*math.tan(3.14/5)
#     total=Area_half/area_second_half
#     print(total)

# def polygon():
    # s = eval(input("Enter s: "))
    # n = eval(input("Enter n: "))
    # area_half = n*s**2
    # area_total_half=4*math.tan(3.14/n)
    # total_area=area_half/area_total_half
    # print(total_area)


# # Function to find character ASCII code Excercise 3.6
# def ASCII():
#     c=eval(input("Enter a ASCII code: "))
#     print("The character is",chr(c))

# #     --------------------------------------------------


# # Function to find character ASCII code Excercise 3.7

# import time

# def random():
#     n1 =int(time.time()) % 25+65
#     n2 =int(time.time())% 25+97
#     print(chr(n1)," ",chr(n2))


# #     --------------------------------------------------


# # Function to find character ASCII code Excercise 3.9

# def pay():
#     name=input("Enter employee's name: ")
#     hours=eval(input("Enter number of hours worked in a week: "))
#     payrate=eval(input("Enter hourly pay rate: "))
#     federal_tax=eval(input("Enter federal tax withholding rate: "))
#     state_tax=eval(input("Enter state tax withholding rate: "))

#     total_pay_in_week= payrate*hours
#     federal_tax_minus=total_pay_in_week/100*federal_tax    
#     state_tax_minus=total_pay_in_week/100*state_tax
#     total_deduction=federal_tax_minus+state_tax_minus
#     total_pay=total_pay_in_week-total_deduction
#     print("Employee name: ",name)
#     print("Hours Worked: ",hours)
#     print("Pay Rate: ",payrate)
#     print("Gross Pay: ",total_pay_in_week)
#     print("Deductions: \n Federal Withholding (20.0%): ",federal_tax_minus)
#     print(" State Withholding (9.0%): ",state_tax_minus)
#     print(" Total Deduction: ",total_deduction)
#     print("Net Total: ",total_pay)




# #     --------------------------------------------------


# # Function to find character ASCII code Excercise 3.10

# def greeks():  
#     print('\u03b1','\u03b2' ,'\u03b3 ','\u03b4 ','\u03b5','\u03b6','\u03b7',' \u03b8')



# #     --------------------------------------------------


# # Function to find character ASCII code Excercise 3.11


# number = int(input("Enter the integer number: ")) 
# revs_number = 0  
# while (number > 0):     
#     remainder = number % 10  
#     revs_number = (revs_number * 10) + remainder  
#     number = number // 10  
# print("The reverse number  : {}".format(revs_number))  
   

