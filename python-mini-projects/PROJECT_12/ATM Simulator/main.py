#ATM simulator


"""
ATM Simulator (OOP)

Features:

create account
deposit
withdraw
check balance
transaction history (bonus)

Use:

classes
methods
loops
files (bonus)
"""

class Account :
    def __init__(self,acc_no,name,pin,balance = 0):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []
    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            self.history.append(f"Deposited : {amount}")
            print(f"{amount} deposited successfully.")
        else :
            print("Invalid amount ! Must be greater than 0.")
    def withdraw(self,amount):
        if amount <= 0 :
            print("Invalid amount!!")
        elif amount > self.balance:
            print("Insufficient balance !!")
        else :
            self.balance -= amount
            self.history.append(f"withdrawn : {amount}")
            print(f"{amount} withdrawn successfully !!")

    def check_balance(self):
        print(f"current balance : {self.balance}")
        return self.balance 
    def show_history(self):
        if len(self.history) ==0 :
            print("No transcation yet.")
        else :
            print("Transcation history :")
            for transcation in self.history :
                print(transcation)

accounts = {}

while True :
    print("\n--- ATM Menu---")
    print("1.Create Account")
    print("2.Login")
    print("3.Exit")
    choice = int(input("Enter the choice : "))

    if choice == 1 :
        acc_no = input("Enter account number :")
        if acc_no in accounts :
            print("Account already exists.")
        else :
            name = input("Enter the name : ")
            pin = int(input("Enter the 4 digits pin"))
            accounts[acc_no] = Account(acc_no,name,pin)
            print("Account created successfully")
    elif choice == 2 :
        acc_no = input("Enter account number :")
        pin = int(input("Enter pin : "))

        if acc_no in accounts and accounts[acc_no].pin == pin :
            user = accounts[acc_no]
            print(f"welcome ,{user.name}")
            while True :
                print("1.Deposit")
                print("2.withdraw")
                print("3.check balance")
                print("4.History")
                print("5.Logout")
                user_choice = int(input("Enter the choice : "))
                if user_choice == 1 :
                    amt = int(input("Enter the amount to deposit :"))
                    user.deposit(amt)
                elif user_choice ==2 :
                    amt = int(input("Enter the amount to withdraw :"))
                    user.withdraw(amt)
                elif user_choice == 3 :
                    user.check_balance()
                elif user_choice == 4 :
                    user.show_history()
                elif user_choice == 5 :
                    print("Logged out")
                    break
                else :
                    print("Invalid choice !")
        else :
            print("Invalid account number or pin.")

    elif choice == 3 :
        print("Thank you for using the ATM.")
        break
    else :
        print("Invalid choice")