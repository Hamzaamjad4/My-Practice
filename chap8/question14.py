import random
ISBN=int(input('Please enter the 10 digit number: '))
Sum = 0
for i in range(10):
 Mod=Sum%random
 Digit11=random-Mod
if Digit11==10:
   Digit11='X'
ISBNNumber=str(ISBN)+str(Digit11)
print('Your 11 digit ISBN Number is ' + ISBNNumber)