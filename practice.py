import random


while True:
      Email = input("Enter your Email: ")
      if "@"and "." in Email:
         print(Email)
         break
      else:
         print("your email is incorrect")     
FullName = input("Enter your name :")
UserName = input("Enter your User Name: ")
r = '{}'.format(random.randint(0, 1000))
print(UserName,r)
Password =input ("Enter your pasword: ")

tag_list=[Email,FullName]
sel= FullName,UserName,Password,Email
all_options = list(map(lambda op: op.text, sel.options))
# print(all_options)

xs= input("enter year")

print(xs, xs in all_options)
if xs in all_options:
    sel.select_by_visible_text(xs)
    print(sel.first_selected_option.text)
else:
    print("this value not exist")








# num = input ("Enter number :")
# print(num)
# name1 = input("Enter name : ")
# print(name1)
  
# # Printing type of input value
# print ("type of number", type(num))
# print ("type of name", type(name1))
# print ("Please share the information asked for:\n" )

# # inputing a string
# name = input("Enter your name:")
# # inputing a number
# age = input("Enter your age:")

# print ("Your name is: " + name);
# # using str method to convert number to string
# print ("and your age is:" + str(age))

# def add(x, y):
#    """This function adds two numbers"""

#    return x + y

# def subtract(x, y):
#    """This function subtracts two numbers"""

#    return x - y

# def multiply(x, y):
#    """This function multiplies two numbers"""

#    return x * y

# def divide(x, y):
#    """This function divides two numbers"""

#    return x / y

# # take input from the user
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# choice = input("Enter choice: 1, 2, 3, or 4: ")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if choice == '1':
#    print(num1,"+",num2,"=", add(num1,num2))

# elif choice == '2':
#    print(num1,"-",num2,"=", subtract(num1,num2))

# elif choice == '3':
#    print(num1,"*",num2,"=", multiply(num1,num2))

# elif choice == '4':
#    print(num1,"/",num2,"=", divide(num1,num2))
# else:
#    print("Invalid input")