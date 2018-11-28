#Hero's Inventory
#Eric Wright
#11/18
import random

player_health = 100
player_armor = 1250
player_attack = 250
player_money = 0

player_stats = ["health", player_health, "armor", player_armor, "attack", player_attack, "money", player_money]

inventory = ["rusty sword", "leather armor","wood shield","small healing potion"]

print("player stats")
print(player_stats)
print()
print("your items:")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")
print("You have", len(inventory), "items in your possession.")

player_health -= 22
input("\nyou have taken some damage on your journey \n"+"your health is at "+str(player_health)+"\n"+"you need to use your healing potion \nPress the enter key to continue.")

if "small healing potion" in inventory:
    print("You will live to fight another day. by using the small healing potion")
    player_health += 20
    print(player_stats)
    inventory.remove("small healing potion")
    for item in inventory:
        print(item)

index = input("\nEnter the index number for an item in inventory: ")
if index.isdigit():
    int(index)
while index.isalnum():
    print("please enter a number")
    index = input("\nEnter the index number for an item in inventory: ")
    if index.isdigit():
        int(index)
while index > len(inventory)-1 or index < 0:
    print("that number is out of range")
    index = input("\nEnter the index number for an item in invertory: ")
    if index.isdigit():
        int(index)
    while index.isalnum():
        print("please enter a number")
        index = input("\nEnter the index number for an item in inventory: ")
        if index.isdigit():
            int(index)
print("At index", index, "is", inventory[index])  

start = input("\nEnter the index number to begin a slice: ")
if start.isdigit():
    int(start)
while start.isalnum():
    print("enter a number please")
    start = input("\nEnter the index number to begin a slice: ")
    if start.isdigit():
        int(start)
while start > len(inventory)-1 or start < 0:
    print("that number is out of range")
    start = input("\nEnter the index number to begin a slice: ")
    if start.isdigit():
        int(start)
    while start.isalnum():
        print("please enter a number")
        start = input("\nEnter the index number to begin a slice: ")
        if start.isdigit():
            int(start)
finish = input("Enter the index number to end the slice: ")
if finish.isdigit():
    int(finish)
while finish.isalnum():
    print("enter a number please")
    finish = input("\nEnter the index number to begin a slice: ")
    if finish.isdigit():
        int(finish)
while finish > len(inventory)-1 or finish < 0:
    print("that number is out of range")
    finish = input("\nEnter the index number to begin a slice: ")
    if finish.isdigit():
        int(finish)
    while finish.isalnum():
        print("please enter a number")
        finish = input("\nEnter the index number to begin a slice: ")
        if finish.isdigit():
            int(finish)
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

chest_items = ["gold", "gems", "elven sword", "bow", "crossbow", "boots", "hat"]
chest = []
for i in range(3):
    item = random.choice(chest_items)
    chest.append(item)
print("You find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print(inventory)

input("\nPress the enter key to continue.")
print("You trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("your inventory is now:")
print(inventory)

input("\n Press the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print(inventory)
input("\nPress the enter key to continue.")
print("in a great battle, your shield is destroyed.")
del inventory[2]
print("Your inentory is now:")
print(inventory)

print("your crossbow and armor are stolen by thieves.")
del inventory[:2]
print(inventory)