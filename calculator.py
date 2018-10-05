#Eric Wright
#10/18
#Calculator Program

thelist = ["Multiply", "multiply", "1", "Divide", "divide", "2", "Add", "add", "3", "Subtract", "subtract", "4"]

def Multiply(x,y):
    z = x * y
    print(z)

def Divide(x,y):
    x = float(x)
    y = float(y)
    z = x / y
    print(z)

def Add(x,y):
    z = x + y
    print(z)

def Subtract(x,y):
    z = x - y
    print(z)

while True:
    operation = input("What would you like to do? Multiply(1) /Divide(2) /Add(3) /Subtract(4) ")
    if operation in thelist:
        break
    else:
        print("That was not an option..")

if operation == "Multiply" or operation == "multiply" or operation == "1":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number...")
    Multiply(x,y)
elif operation == "subtract" or operation == "Subtract" or operation == "4":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Subtract(x,y)
elif operation == "Add" or operation == "add" or operation == "3":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number..")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Add(x,y)
elif operation == "Divide" or operation == "divide" or operation == "2":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Divide(x,y)
else:
    pass