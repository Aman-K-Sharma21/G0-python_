# 1. Get the inputs from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# 2. Check the operator and perform the correct calculation
if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operator == "/":
    # A quick check to prevent a crash from dividing by zero!
    if num2 == 0:
        print("Error: You cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    print("Error: Invalid operator! Please use +, -, *, or /.")