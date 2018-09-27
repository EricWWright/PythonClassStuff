name = input("what is your name? ").title()
age = input("what is your age? ")

if name.isalpha() and age.isdigit() and age >= "18" or name == "Eric":
    print("yo the name u enter is:", name, "ur age is:", age)
    print("Welcome to the club", name)
else:
    print("What are you doing m8? You are not aloud to enter the club...")

if age < "65" or age > "16" and age.isdigit():
    print(name, "can drive")
elif age > "65":
    print(name,"you can't drive you are too old and cant see")
elif age < "16":
    print(name,"you are too young to drive you need to grow up some more")
else:
    print("um....Reeeeeeeeeeeeeeeeeeeeeeeee you shouldn't be driving")


# num1: input for the user; cast to int
# num2: input from the user; cast to int
# check number if num1 and num2 are all digits
# if both are digits tell user (compound if)
# if ore or ethe other is a digit tell user
# if neither are digits tell user

num1 = input("enter number: ")
num2 = input("enter another number: ")

if num1.isdigit() and num2.isdigit():
    print("Both", num1, num2, "are digits!")
elif num1.isdigit():
    print("only", num1, "is a digit")
elif num2.isdigit():
    print("only", num2, "is a digit")
else:
    print("none of what you entered was a number...")

