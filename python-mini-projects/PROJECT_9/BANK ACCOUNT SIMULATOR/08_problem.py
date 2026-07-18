# The previous script runs automatically and stops. In the real world, software uses a Loop to keep running until the user decides to quit.

class BankAccount :
    def __init__(self,account_holder,initial_balance = 0.0) :
        self.holder = account_holder
        self.balance = initial_balance
        print(f"Account created succesfully for {self.holder}!")

    #Method to deposit money

    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            print(f"{amount} deposit successfully.")
            self.check_balance()
        else :
            print("Invalid deposit amount !Please enter a positive number")

    #Method to withdraw money

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
            self.check_balance()
        else:
            print("invalid withdrawl amount!")

    #Method to check the current account balance

    def check_balance(self):
        print(f"current balance for {self.holder} : {self.balance}")


print("---Welcome to the Bank---")
name = input("Enter your name to open an account : ")
account = BankAccount(name)

while True :
    print("\n1.Deposit")
    print("\n2.withdraw")
    print("\n3.check balance")
    print("\n4.Exit")
    choice = int(input("Choose an option (1-4) : "))

    if choice == 1 :
        amt = float(input("Enter amount to deposit : "))
        account.deposit(amt)

    elif choice == 2 :
        amt = float(input("Enter amount to withdraw : "))
        account.withdraw(amt)

    elif choice ==3 :
        account.check_balance()

    elif choice == 4 :
        print(f"\n Thank you for using our bank {name}. Goodbye !")
        break

    else :
        print("invalid choice !Please enter a number between 1 and 4.")
        