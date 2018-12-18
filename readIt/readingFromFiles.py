# read it program
# working with reading from a file
# Eric Wright
# 12/18

def main():
    # print("opening the file")
    # text_file = open("read_it.txt","r")
    # text_file.close()
    # input()

    # print("\nReading characters from the file.")
    # text_file = open("read_it.txt","r")
    # print(text_file.read(1))
    # print(text_file.read(5))
    # text_file.close()
    # input()

    # text_file = open("read_it.txt","r")
    # print(text_file.read(5))
    # text_file.close()
    # input()

    # text_file = open("read_it.txt","r")
    # whole_thing = text_file.read()
    # print(whole_thing)
    # text_file.close()
    # input()

    # print("\nReading characters from a line.")
    # text_file = open("read_it.txt","r")
    # print(text_file.readline(1))
    # print(text_file.readline(5))
    # text_file.close()
    # input()

    # print("\nReading one line at a time.")
    # text_file = open("read_it.txt","r")
    # print(text_file.readline())
    # print(text_file.readline())
    # print(text_file.readline())
    # text_file.close()
    # input()

    # print("\nReading the entire file into a list.")
    # text_file = open("read_it.txt", "r")
    # lines = text_file.readlines()
    # print(lines)
    # print(len(lines))
    # for line in lines:
    #     print(line)
    # text_file.close()
    # input()

    print("\nLooping through the file, line by line.")
    text_file = open("write_it.txt","r")
    count = 0
    for line in text_file:
        count += 1
        print(line)
    text_file.close()
    print(count)
    input()

main()