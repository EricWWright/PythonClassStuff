#Eric Wright
# 9/18
def get_name():

    #ask user for name
    name = input("What is your name? ")

    #display name
    print("the name you entered was", name)

print("this is our function")
get_name()

def circleArea():
    PI = 3.14159265359

#1 get a radius
    x = input("what is the radius? ")

#2 compute the area
    x = float(x)
    area = x * x * PI

#3 display information back
    print("the area of the circle is:", area)

circleArea()

varStop = input("End Program")