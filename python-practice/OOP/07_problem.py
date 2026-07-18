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


print("----Opening Account----")
user1_acc = BankAccount("Aman",2000.0)
user2_acc = BankAccount("Rohit")

print("----Aman Transcation----")

user1_acc.check_balance()
user1_acc.deposit(500)
user1_acc.deposit(300)
user1_acc.withdraw(400)


print('---Rohit transcation----')

user2_acc.check_balance()
user2_acc.deposit(1500)

