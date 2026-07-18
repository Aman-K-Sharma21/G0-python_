import save_expense, read_expense, monthlytotal

def main():
    
    while True:
        print("-----Mini Expense tracker-----")
        print("-"*25)
        print("1.Add Expense ")
        print("2.Show expenses and total ")
        print("3.Show monthly totals ")
        print("4.Exit")
        print("="*70)
        choice = int(input("Enter(1-4), what do you want to do today : "))

        if choice == 1:
            item = input("what did you buy today : ").strip() #strip remove unwanted space and put string inside inverted commas
            if "," in item or not item:
                print("Invalid name!")
                continue

            try:
                cost = float(input("How much does it cost : $"))
                if cost <0:
                    print("cost can't be negative")
                    continue
                save_expense(item,cost)
                print(f"Saved {item} succesfully")

            except ValueError:
                print("Please type a valid number.")

        elif choice == 2:
            read_expense()

        elif choice == 3:
            monthlytotal()

        elif choice == 4:
            print("_____________Good Bye_______________")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()





