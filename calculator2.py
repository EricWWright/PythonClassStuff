#Eric Wright
#10/18
#Calculator Program

def multiply(x,y):
    float(x)
    float(y)
    z = x * y
    print("Here is your answer:", z)
    
def divide(x,y):
    if y != 0:
        float(x)
        float(y)
        z = x / y
        print("Here is your answer:", z)
    else:
        print("Enter valid input")
        divide(x,y)

def add(x,y):
    float(x)
    float(y)
    z = x + y
    print("Here is your answer:", z)

def subtract(x,y):
    float(x)
    float(y)
    z = x - y
    print("Here is your answer:", z)

def main():
    print("Select a operation")
    print("\n Multiply (1)\n Divide (2)\n Add (3)\n Subtract (4)\n")
    answer = input()
    if answer == "Multiply" or answer == "multiply" or answer == "1":
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        multiply(x,y)
    elif answer == "Divide" or answer == "divide" or answer == "2":
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        divide(x,y)
    elif answer == "Add" or answer == "add" or answer == "3":
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        add(x,y)
    elif answer == "Subtract" or answer == "subtract" or answer == "4":
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        subtract(x,y)
main()
