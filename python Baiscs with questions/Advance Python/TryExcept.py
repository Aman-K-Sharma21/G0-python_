#try and except excepting handling



number1 = input("Enter the number :") # 45
number2 = input("Enter the number :") # asdfd

try:
    print(f"The sum of {number1} and {number2} is : ", int(number1) + int(number2))
except Exception as e:
    print(e)
    print("Please enter only numeric element only")
    

print("This is very important line")