year = int(input("Year: "))
while not int(year) in range(1583, 10000):
    year = input("Out of allowed range 1583 - 9999. Please enter a valid number: ")

month = int(input("Month: "))
while not int(month) in range(1, 13):
 month = input("Out of allowed range 1 - 12. Please enter a valid number: ")

if month == 1 or month == 2:
 month += 12
 year -= 2

day = int(input("Day: "))
while not int(day) in range(1, 32):
        day = input("Out of allowed range 1 - 31. Please enter a valid number: ")


result = ( day + 13 * (month+1) // 5 + year + year // 4 - year// 100 + year // 400 ) % 7


weekday = {0: "Saturday",1: "Sunday", 2: "Monday",3: "Tuesday",4: 
"Wednesday",5: "Thursday",6: "Friday"}

print("The day is " + weekday[int(result)] + ".")