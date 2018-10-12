#Eric Wright
#10/18
#loops
import random

# loops = 0
# while True:
#     print("I have looped", loops, "times")
#     loops += 1
#     if loops == 100000:
#         break

# count = 0
# while True:
#     count += 1
#     if count > 100:
#         break
#     if count == 5 or count == 25 or count == 50:
#         continue
#     print(count)
    
# i = 0
# while i != 1000:
#     print("looping")
#     i += 1
    
# i = 0
# while i <= 1000:
#     print("Looping")
#     i += 1
    
# i = "enter"
# while i == "enter":
#     print("Loopy loop")
#     x = input("do you want to keep looping yes or no")
#     if x == "yes":
#         continue
#     elif x == "no":
#         i = " "
    
# print("Your lone hero is surrounded by a massive army of trolls.")
# print("Their decaying green bodies stretch out, melting to the horizon.")
# print("Your hero unsheathes his sword for the fast fight if his life.\n")

# health = 10
# trolls = 0
# damage = 3

# while health >= 0:
#     trolls += 1
#     health -= damage
#     print("Your hero swings and defeats an evil troll, "\
#         "but takes", damage, "damage points.\n")
    
# print("Your hero fought valiantly and defeated", trolls, "trolls.")
# print("But alas, your hero is no more.")
    
win = 0
mHealth = 100
pHealth = 100

choice = input("attack or run ")
while choice == "attack":
    pDamage = random.randrange(0, 25)
    mDamage = random.randrange(0, 50)
    print("you attack the monster for", pDamage, "health")
    mHealth -= pDamage
    if mHealth > 0:
        pHealth -= mDamage
        print("the monster attacks you for", mDamage, "health")
    if pHealth <= 0:
        win = 0
        print("you died")
        break
    elif mHealth <= 0:
        win = 1
        print("you have killed the monster")
        break
    elif pHealth >= 0 and mHealth >= 0:
        print("you have", pHealth, "health")
        print("the monster has", mHealth, "health")
        choice = input("attack or run ")
    if choice != "attack" or choice != "run":
        print("i'm not sure what that is")
        choice == "attack"
        continue
    if choice == "run":
        win = 0
        print("you are a coward")
    if win == 0:
        input("Game Over")
    elif win == 1:
        input("You Won")
    else:
        continue
            
input("\n\n press enter to exit")
    
