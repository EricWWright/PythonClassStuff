# def get_grade():
#     grade = int(input("Enter a grade:"))
#     return grade

# grade1 = get_grade()
# grade2 = get_grade()
# grade3 = get_grade()
# grade4 = get_grade()
# grade5 = get_grade()

# sum = grade1 + grade2 + grade3 + grade4 + grade5
# average = sum / 5
# print("the average is:", average)

# gradelist = []

# def getGrade(gradelist):
#     maxGrade = 100
#     while True:
#         grade = input("enter a grade to exit press space bar")
#         if grade == " ":
#             break
#         else:
#             x = float(grade)
#             if grade.isdigit() and x <= maxGrade:
#                 grade = float(grade)
#                 gradelist.append(grade)
#             elif x >= maxGrade:
#                 q = input("are you sure this", grade, "is a good grade y or n")
#                 if q == "y":
#                     grade = float(grade)
#                     gradelist.append(grade)
#                 else:
#                     print("that is not a good grade") 
#             else:
#                 print("that's not a good grade")

# def avgfunction(gradelist):
#     sumgrade = 0
#     for grade in gradelist:
#         sumgrade += grade
#     avg = sumgrade / len(gradelist)
#     return avg

# def main(gradelist):
#     getGrade(gradelist)
#     avg = avgfunction(gradelist)
#     print("your grade is", avg)

# main(gradelist)

start = 0
stop = 10000
stepvalue = 1

for i in range(start,stop,stepvalue):
    print(i)