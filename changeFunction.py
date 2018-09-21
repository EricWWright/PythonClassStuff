#Eric Wright
#9/18
#change sorter

#first function is off by default
def change():
    #1 get input from user for how much change
    totalChange = int(input("How much change do you have in your pocket?: "))
    #2 calculate total for quarter nickles dimes pennys
    quarters = totalChange // 25
    whatsLeft = totalChange % 25
    dimes = whatsLeft // 10
    whatsLeft = whatsLeft % 10
    nickles = whatsLeft // 5
    whatsLeft = whatsLeft % 5
    cents = whatsLeft
    #3 display it back to the user
    print("\nQuarters:", quarters, "\nDimes:", dimes, "\nnickles:", nickles, "\nPennys:", cents)

i = 0

while i == 0:
    change()
    stop = int(input("\nIf you would like to stop the program type 1\n If you would continue running the program type 0: "))
    i = stop

def change2(totalChange):
    #1 get input from user for how much change
    totalChange = totalChange
    #2 calculate total for quarter nickles dimes pennys
    quarters = totalChange // 25
    whatsLeft = totalChange % 25
    dimes = whatsLeft // 10
    whatsLeft = whatsLeft % 10
    nickles = whatsLeft // 5
    whatsLeft = whatsLeft % 5
    cents = whatsLeft
    #3 return value
    return quarters, dimes, nickles, cents

totalChange = int(input("How much change do you have in your pocket?: "))
quarters, dimes, nickles, cents = change2(totalChange)
print("\nQuarters:", quarters, "\nDimes:", dimes, "\nnickles:", nickles, "\nPennys:", cents)