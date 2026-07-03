def monthly_total():
    try:
        with open("expense.txt") as f:
            totals = {}
            for line in f:
                cleared_line = line.strip()
                if cleared_line:
                    item,cost_str,month = cleared_line.split(",")
                    cost = float(cost_str)
                    totals[month] = totals.get(month,0) + cost
            if not totals:
                print("\nNo expenses recorded yet.")
                return

            print("--MONTHLY TOTALS--")
            for month in sorted(totals):
                print(f"{month} : ${totals[month]:.2f}")
            print("-"*25)
    except FileNotFoundError:
        print("\nNo expenses recorded yet. Your file is empty!")