# Function to convert celsius into ferenheit Excercise 1.1
# def forenheit():
#     celsius=eval(input("Enter Temprature in celsius: "))
#     forenheit=(9/5)*celsius+32
#     print(forenheit)


#     --------------------------------------------------


# Function to find volume of Radius Excercise 2.2 
# def volume():
#     radius=eval(input("Enter Radius: "))
#     length=eval(input("Enter length: "))
#     area=radius*radius*3.14
#     volume=length*area
#     print("The area is",area,"The Volume is",volume)

#     --------------------------------------------------



# Function to convert feet into meter Excercise 2.3
# def feet():
#     feet=eval(input("Enter Value in Feet: "))
#     meter=feet/3.28
#     print(meter)
# feet()

#     --------------------------------------------------



# Function to convert pounds into kilograms Excercise 2.4
# def pounds():
#     pounds=eval(input("Enter Value in pounds: "))
#     Kg=pounds*0.454
#     print(pounds,"pounds is",Kg,"kilograms")

#     --------------------------------------------------


# Function To find gratuity Excercise 2.5
# def gratuity():
#     gratuity,rate=eval(input("Enter the subtotal and a gratuity rate: "))
#     total=gratuity/100*rate
#     print(total)
# gratuity()


#     --------------------------------------------------

# Function to find sum of digit Excercise 2.6
# def getSum():
#     while True:
#         try:
#             sum=0
#             n=eval(input("Enter a number between 0-1000: ")) 
#             if 0 < n <= 1000:
#                 for digit in str(n): 
#                     sum += int(digit)      
#             print(sum)    
#             break
#         except:
#             print("Enter Wrong Number")


#     --------------------------------------------------


# Function to find number of years and days Excercise 2.7
# # import time
# # minutes = eval(input("enter minutes"))
# # hours = minutes // 1440
# # days = hours // 34560
# # print(days)
# number_of_days = int(input("Enter number of days: "))
# # Calculating years
# years = number_of_days // 365

# # Calculating months
# months = (number_of_days - years *365) // 30

# # Calculating days
# days = (number_of_days - years * 365 - months*30)

# # Displaying results
# print("Years = ", years)
# print("Months = ", months)
# print("Days = ", days)


#     --------------------------------------------------

# Function to find energy needed Excercise 2.8
# def energy():
#     amount_of_water = int(input("Enter amount of water in kg: "))
#     initial_temp =int(input("Enter initial temp: "))
#     final_temp = int(input("Enter final temp: "))
#     Q = amount_of_water * (final_temp-initial_temp) * 4184
#     print(Q)

# Function to find wind chill index Excercise 2.9
# def temp():
#     while True:
#         try:
#             temperature =float (input("Enter Temperature: "))
#             wind = float(input("Enter wind: ")) 
#             if -58 < temperature <= 41:
#                 total=35.74+0.6215*(temperature)-35.75*(wind)**0.16+0.4275*(temperature)*(wind)**0.16
#             print(total)
#             break
            
#         except:
#             print("Enter correct number")
#             break


# def investment():
#     final_amount=eval(input("Enter final Amount: "))
#     annual_interest=eval(input("Enter annual Interest rate: "))
#     years=eval(input("Enter number of years"))
#     power=years*12
#     annual_interest_one_added=1+(annual_interest/12)
#     power_of_monthly_intrest=annual_interest_one_added**power
#     deposite_value=final_amount/power_of_monthly_intrest
#     print(power_of_monthly_intrest)
# investment()    



# def reverse():
#     number1 = int(input("Enter the integer number: "))  
#     number2 = int(input("Enter the integer number: "))  

#     number3 = int(input("Enter the integer number: "))  
#     print(number3)
#     print(number2)
#     print(number1)

  
# def table():
#     d = {1: [1, 33.2,1 ],
#     2: [2, 23, 2],
#     3: [3, 17, 3],
#     10: [4, 10, 42],
#     5: [5, 9, 512],
#     6: [6, 1, 1236] }
#     print ("{:<15} {:<10} {:<10}".format('a','b','a**b'))
#     for k, v in d.items():
#         lang, perc, change = v
#         print ("{:<15} {:<10} {:<10}".format(lang, perc, change))

# import math
# def hexagon():
#     hexagon = eval(input("Enter the integer number: ")) 
#     total=3*math.sqrt(3)/2*hexagon**2
#     print(total)


# def accelration():
#     v0,v1,t=eval(input("Enter v0,v1 and t: "))
#     accelration=v1-v0/t
#     print(accelration)
# accelration()
def dmi():
    weight,height=eval(input("Enter weight and height: "))
    dmi=weight/height/height*703
    print(dmi)
dmi()