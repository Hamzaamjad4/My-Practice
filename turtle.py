from tabulate import tabulate
# import turtle

# #Excercise 1.1 by using function
def one():
    print("Welcome to python programming")

# #Excercise 1.2 by using function and forloop
def two():
    for i in range(2):
        print("Welcome to python programming")
# # Excercise 1.3 by using function
def three():
    result_str="";    
    for row in range(0,5):    
        for column in range(0,8):     
            if (((column == 1 ) or (column == 5 and row!=1 and row!=4 and row!=3)  )  or ((row == 0 or row == 2) and (column > 1 and column < 5 ))):    
                result_str=result_str+"F"    
            else:      
                result_str=result_str+" "    
        result_str=result_str+"\n"   
    print(result_str); 
   
    result_strr="";
    for row in range(0,4):    
        for column in range(0,8):    
            if (((column == 0 ) or (column == 7 ) or (row==3 and column!=0  )  )  ):    
                result_strr=result_strr+"*"    
            else:      
                result_strr=result_strr+" "    
        result_strr=result_strr+"\n"    
    print(result_strr);   

    result_N="";
    for row in range(0,4):    
        for column in range(0,8):    
            if (((column == 0 ) or (column == 7 )or(row==1 and column!=1 and column!=3 and column!=4 and column!=5 and column!=6) or 
            (row==2 and column!=1 and column!=2) and column!=3 and column!=5 and column!=6)  ):    
                result_N=result_N+"*"    
            else:      
                result_N=result_N+" "    
        result_N=result_N+"\n"    
    print(result_N); 

# #Table by using function
def table ():
    table = [['a', 'a^2', 'a^3'], [1, 1, 1], [2, 4, 8], [3, 9, 28]]
    print(tabulate(table))
 


# # Divide multiply expression by using function 
def expression():
    number=9.5*4.5-2.5*3/45.5-3.9
    print(number)

def expression2():
    number=1+2+3+4+5
    print(number)

def expression2():
    number=4*(1-1/3+1/2)
    print(number)

#Turtle Excercise
# turtle.color("blue")
# turtle.penup()
# turtle.goto(25,25)
# turtle.pendown()
# turtle.down(1)
# turtle.done()
# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# skk = turtle.Turtle()
# turtle.forward()
# turtle.left(90)
# turtle.goto(0)
# turtle.pendown()
# turtle.right(100)
# turtle.done()

  

# #window shap with turtle

# t = turtle.Turtle()  
# t.forward(100)
# t.left(90) 
# t.forward(100)
# t.left(90) 
# t.forward(100) 
# t.left(90) 
# t.forward(100) 
# t.left(90) 
# t.forward(50)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(100)


one()