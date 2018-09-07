import random
min = 1
max = 20

roll_again = input("Would you like to roll the dice?")


while roll_again == "yes" or roll_again == "y":
    print ("Rolling the die...")
    print ("You Rolled A....")
    print (random.randint(min, max))
    
    roll_again = input("Would you like to roll the dice?")
    
