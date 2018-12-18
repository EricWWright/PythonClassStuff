# Write It
# Demonstrates writing to a text file
# Eric Wright
# 12/18

def main():
    text_file = open("write_it.txt","w")
    text_file.write("Line 1\n")
    text_file.write("This is line 2\n")
    text_file.write("That makes this line 3\n")
    text_file.close()
    input("Press enter to rewrite the file with scores")

    # Creating a text file with the writelines() method
    print("\nCreationg a text file with the writelines() method.")
    text_file = open("write_it.txt","w")
    lines = ["score1\n","score2\n","score3\n","score4\n","score5\n"]
    text_file.writelines(lines)
    text_file.close()

main()