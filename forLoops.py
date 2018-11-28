# word = input("enter a word ")
# print("\nHere's each letter in your word:")
# for letter in word:
#     print(letter)

# message = input("Enter a message: ")
# new_message = ""
# VOWELS = "aeiou"
# for letter in message:
#     if letter.lower() not in VOWELS:
#         new_message += letter
#         print("A new string has been created:", new_message)
# print("\nYour message without vowels is:", new_message)

# input("\n\nPress Enter to exit")

NUM128 = 128
NUM64 = 64
NUM32 = 32
NUM16 = 16
NUM8 = 8
NUM4 = 4
NUM2 = 2
NUM1 = 1

day_set1=""
day_set2=""
day_set4=""
day_set8=""
day_set16=""

whatsLeft = 0

for i in range(1,32):
    bia_num = ""
    input_num = i
    whatsLeft = input_num
    if (input_num >= NUM128):
        whatsLeft = input_num - NUM128
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"
    
    if (whatsLeft >= NUM64):
        whatsLeft = whatsLeft - NUM64
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if (whatsLeft >= NUM32):
        whatsLeft = whatsLeft - NUM32
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"
    
    if (whatsLeft >= NUM16):
        whatsLeft = whatsLeft - NUM16
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"
    
    if (whatsLeft >= NUM8):
        whatsLeft = whatsLeft - NUM8
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if (whatsLeft >= NUM4):
        whatsLeft = whatsLeft - NUM4
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if (whatsLeft >= NUM2):
        whatsLeft = whatsLeft - NUM2
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if (whatsLeft >= NUM1):
        whatsLeft = whatsLeft - NUM1
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    xnum7 = bia_num[7]
    xnum6 = bia_num[6]
    xnum5 = bia_num[5]
    xnum4 = bia_num[4]
    xnum3 = bia_num[3]
    xnum2 = bia_num[2]
    xnum1 = bia_num[1]
    xnum0 = bia_num[0]
    
    x=str(i)
    if xnum3 == "1":
        day_set1 = day_set1 + x + " "
    if xnum4 == "1":
        day_set2 = day_set2 + x + " "
    if xnum5 == "1":
        day_set4 = day_set4 + x + " "
    if xnum6 == "1":
        day_set8 = day_set8 + x + " "
    if xnum7 == "1":
        day_set16 = day_set16 + x + " "

actualBday = 0
print(day_set1)
#bday1 = input("Is your birthday in this set of numbers (yes or no)")
print(day_set2)
#bday2 = input("Is your birthday in this set of numbers (yes or no)")
print(day_set4)
#bday3 = input("Is your birthday in this set of numbers (yes or no)")
print(day_set8)
#bday4 = input("Is your birthday in this set of numbers (yes or no)")
print(day_set16)
#bday5 = input("Is your birthday in this set of numbers (yes or no)")

# if bday1 == "yes":
#     actualBday = actualBday + 1
# if bday2 == "yes":
#     actualBday = actualBday + 2
# if bday3 == "yes":
#     actualBday = actualBday + 4
# if bday4 == "yes":
#     actualBday = actualBday + 8
# if bday5 == "yes":
#     actualBday = actualBday + 16
# print("Is your birthday", actualBday,'?')
