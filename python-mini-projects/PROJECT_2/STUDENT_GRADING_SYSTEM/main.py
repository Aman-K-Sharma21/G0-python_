
#Student grading system..............

def student_result():

    name = input("Enter the student name :")
    marks = int(input("Enter the total of best of 5 subject score  :"))
    percentage = (marks/500)*100

    if percentage >=33 and percentage <=39:
        print("congratulation,you passed the examination.")
        print(f"your percentage is : {percentage}")
        print("your grade is D")
    
    elif percentage >=40 and percentage <=49:
        print("congratulation,you passed the examination.")
        print(f"your percentage is : {percentage}")
        print("your grade is C2")
    
    elif percentage >=50 and percentage <=59:
        print("congratulation,you passed the examination.")
        print(f"your percentage is : {percentage}")
        print("your grade is C1")
    
    elif percentage >=60 and percentage <=69:
        print("congratulation,you passed the examination.")
        print(f"your percentage is : {percentage}")
        print("your grade is B2")
    
    elif percentage >=70 and percentage <=79:
        print("congratulation,you passed the examination.")
        print(f"your percentage is : {percentage}")
        print("your grade is B1")
    
    elif percentage >=80 and percentage <=90:
        print("congratulation,you passed the examination.")
        print(f"your percentage is : {percentage}")
        print("your grade is A2")
    
    elif percentage >=91 and percentage <=100:
        print("congratulation,you passed the examination.")
        print(f"your percentage is : {percentage}")
        print("your grade is A1")
    else:
        print("Sorry ,you have the class. Try next year")
        print(f"your percentage is : {percentage}")
        print("your grade is F")


student_result()