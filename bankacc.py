class Bank_acc(object):

    def __init__(self, name):
        self.account_num = int(input("Enter your account number"))
        self.phone_num = int(input("Enter your phone number"))
        self.pin_num = 123456789
        self.balance = 0
        self.name = name

    def credit_acc(self):
        get_pin = int(input("Please enter your pin"))
        while True:
            if get_pin != self.pin_num:
                get_pin = int(input("Please enter your pin"))
            else:
                ammount = int(input("How much do you want to add to your account"))
                self.balance += ammount
                break

    def debit_acc(self):
        get_pin = int(input("Please enter your pin"))
        while True:
            if get_pin != self.pin_num:
                get_pin = int(input("Please enter your pin"))
            else:
                ammount = int(input("How much do you want to withdraw from your account"))
                while True:
                    if ammount <= self.balance:
                        self.balance -= ammount
                        break
                    else:
                        print("You don't have enough mone")
                    break


erics_acc = Bank_acc("Eric")
print(erics_acc.name)
print(erics_acc.account_num)
print(erics_acc.balance)
erics_acc.credit_acc()
