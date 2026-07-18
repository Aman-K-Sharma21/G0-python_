
while True :
        print("-------CALCULATOR-------")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")

        choose = int(input("Choose an option :  "))
                
        if choose == 5 :
                print("Thank you ! To see the history of recent calculation ,open cal_history.txt file")
                break
        if choose > 5 or choose < 1 :
                print("please enter the choice between 1-5.")
                continue
        num1 = int(input("Enter the number :"))
        num2 = int(input("Enter the number :"))

        if choose ==1 :
                result = num1 + num2 
                calculation = f"{num1} + {num2} = {result}"
        elif choose ==2 :
                result = num1 - num2 
                calculation = f"{num1} - {num2} = {result}"
        elif choose ==3 :
                result = num1 * num2 
                calculation = f"{num1} X {num2} = {result}"
        elif choose ==4 :
                if num2 ==0:
                        print("Can't be divided by zero")
                        continue
                result = num1 / num2 
                calculation = f"{num1} / {num2} = {result}"
        
        print(calculation)

        with open("cal_history,txt","a") as f :
                f.write(calculation + "\n")
        