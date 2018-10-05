# Colton Northcutt and Eric Wright 
# 5 October 2018
# Text adventure

# directions
north = ['north', 'n', 'go north']
south = ['south', 's', 'go south']
east  = ['east', 'e', 'go east']
west = ['west', 'w', 'go west']

# actions
down = ['down', 'd', 'go down']
up = ['up', 'u', 'go up', 'stand up', 'get up']

# start room
def gameStart():
    print("Welcome to Text Adventure!")
    print("Game Start")
    print("You wake up all alone in a dimly lit room. You are currently laying in a bed and find your body is quite sore.")
    print("What do you do?")
    userInput = input().lower()
    if userInput in up:
	    print("\n You get out of the bed and stand up. You are in the middle of the room. \n What do you do?")
        userInput2 = input().lower()
        if userInput2 in north:
            gameStartNorth()
        elif userInput2 in south:
            gameStartSouth()
    elif userInput in north or userInput in south or userInput in east or userIput in west or userInput in down:
        print("You are lying in bed, you can't move in that direction")
        gameStart()
    else:
        print("That is not a recognized command")
        gameStart()

def gameStartNorth():
    print("You go to the the north side of the room where you find a door.")

def gameStartSouth():
    print("You go to the south side of the room where you find a table.")
    print("On the table you find a key")
            
            
gameStart()