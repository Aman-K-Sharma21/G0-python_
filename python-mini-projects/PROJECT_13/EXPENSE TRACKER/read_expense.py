FILENAME = "expense.txt"
def read_expense():
    try:
        with open(FILENAME) as f:
            print("--CURRENT EXPENSE--")
            total = 0
            for line in f:
                cleared_line = line.strip()
                if cleared_line:
                    item,cost_str,month = cleared_line.split(",")
                    cost = float(cost_str)
                    print(f"{item} : ${cost} ({month})")
                    total +=cost
            print("-"*25)
            print(f"Total expense : $ {total}")
    except FileNotFoundError :
        print("\n No expense recorded yet. Your file is empty!")

