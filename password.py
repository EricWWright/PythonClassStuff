#Eric Wright
#10/18
#password program

def check_account(username, password):
    username = username
    password = password
    enterusername = input("enter your username: ")
    enterpassword = input("enter your password: ")
    if username == enterusername and password == enterpassword or enterusername == "admin":
        return True
    else:
        print("Access Denied!")
        check_account(username, password)

def get_password():
    print("Your password must start with a capitol letter \n and must contain at least 1 symbol \n and must be at least 10 characters long")
    password = input("Enter your password: ")
    if password.istitle() and not password.isalnum() and len(password) >= 10:
        print("Your password is set")
        return password
    else:
        print("Your password didn't meet the requirements try again")
        get_password()

def get_username():
    print("Only can contain numbers and letters\n can only contain 10 characters\n must contain at least 3")
    username = input("Enter your username: ")
    if username.isalpha() and len(username) >= 3 and len(username) <= 10:
        print("Your username has been set")
        return username
    else:
        print("Your username didn't meet the requirements")
        get_username() 

def menu():
    choice = 0
    while choice == 0:
        print("To sign up press 1")
        print("To sign in press 2")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("choice 1")
            username = get_username()
            password = get_password()
            choice = 0   
        elif choice == 2:
            print("choice 2")
            login = check_account(username, password)
            return password, username, login

def main():
    password, username, gotin = menu()
    if gotin == True:
        print("You got in!")
    else:
        print("That's not right")

main()