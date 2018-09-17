#Eric Wright
#9/18
import math

# get a users name
def get_name(name_input):
    name = name_input
    name = name.lower()
    name = name.title()
#step two display the name back for user
    print("The name you entered was", name)
#step three verify the name
print("this is our function")
name = input("what's your name? ")
get_name(name)

def circleArea(radius1):
    PI = 3.14159265359   
#1 get a radius
    radius = radius1
#2 compute the area
    radius = float(radius)
    area = radius * radius * PI
#3 display information back
    print("the area of the circle is:", area)

def pythagorasTherom(ap, bp):
    #a^2 + b^2 = c^2
    a = float(ap)
    b = float(bp)
    c = math.sqrt(a+b)
    print("the third side is",c)

def add_numbers(num1p, num2p):
    num1 = num1p
    num2 = num2p
    num3 = int(num1) + int(num2)
    return num3

question1 = input("Would you like to get the area of a circle? ")
if question1 == "yes" or question1=="y" or question1=="sure":
    radiusx = input("What is the radius ")
    circleArea(radiusx)
    
if question1 == "no" or question1=="nope" or question1=="n":
    question2 = input("Would you like to get the side of a triangle? ")

if question2 == "yes" or question2=="y" or question2=="sure":
    ax = input("Enter the first side of the triangle ")
    bx = input("Enter the second side of the triangle ")
    pythagorasTherom(ax, bx)

if question2 =="no" or question2=="nope" or question2=="n":
    question3 = input("Would you like to add two numbers together? ")

if question3 =="yes" or question3=="y" or question3=="sure":
    num1x = input("enter a number ")
    num2x = input("enter another number ")
    num4=add_numbers(num1x, num2x)
    print("the sum of your numbers are", num4)

if question3 =="no" or question3=="nope" or question3=="n":
    print("Okay bye")
    varStop = input("End Program")


