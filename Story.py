import random

# A small 20 sided die rolling program
def AttackDie():
    min = 1
    max = 20

    roll_again = input("Would you like to roll the die?")


    while roll_again == "yes" or roll_again == "y":
        print ("Rolling the die...")
        print ("You Rolled A....")
        print (random.randint(min, max))
        roll_again == "no"

start = input("Should we play through a story?")
if start == "yes" or start == "sure" or start == "y":
    print ("Lets get into it...")
    print ("In a desolate land called the bogenlands you wake up, you find "+
           "your self alone  in some small underground hut lying in bed what do you do?")
    firstChoice = input("1.Get up |OR| 2.Stay in bed and go back to sleep")
else:
    print ("go to sleep forever")

if firstChoice == "1":
    print ("You decide to get up, and find yourself quite groggy.")
    print ("On the night stand next to the bed there is a ___ ")
    pickUp = input("Would you like to pick it up?")

if firstChoice == "2":
    print ("You decide to fall back to sleep...")
    print ("FOREVER...")

if pickUp == "yes" or pickUp == "sure" or pickUp == "y":
    print ("___ has been added to your inventory")
    AttackDie()
else:
    print ("You decided not to pick up ___ and walked away")
