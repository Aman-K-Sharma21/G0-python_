import datetime

FILENAME = "expense.txt"

def save_expense(item, cost):
    month = datetime.date.today().strftime("%Y-%m")
    with open(FILENAME, "a") as f:
        f.write(f"{item},{cost},{month}\n")