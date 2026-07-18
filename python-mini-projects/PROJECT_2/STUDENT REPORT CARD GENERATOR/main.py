#student report card generator 

while True :
    print("------Welcome to Student report card generator-----")
    print("1.Add student")
    print("2.Show All Report")
    print("3.Exit")

    choose = int(input("enter the choice :"))
    
    if choose == 1 :
        #Enter the name of the student,one at a time
        name = input("Enter the name of the student :")
        #Enter the best of five marks one by one
        marks1 = int(input("Enter the marks of 1st subject :"))
        marks2 = int(input("Enter the marks of 2nd subject :"))
        marks3 = int(input("Enter the marks of 3rd subject :"))
        marks4 = int(input("Enter the marks of 4th subject :"))
        marks5 = int(input("Enter the marks of 5th subject :"))

        #format to print name along with marks
        line = f"{name},{marks1},{marks2},{marks3},{marks4},{marks5}\n"

        #To write the entered name and marks of the student
        with open("student.txt","a") as f:
            f.write(line)
        print("---------Student added successfully-----------")
        print("Help - To check the added student details ,open the 'student.txt' file")

    if choose ==2 :
            with open("student.txt") as f:
                lines = f.readlines()
            for line in lines:
                data = line.strip().split(",")
                name = data[0]
                marks1 = int(data[1])
                marks2 = int(data[2])
                marks3 = int(data[3])
                marks4 = int(data[4])
                marks5 = int(data[5])

                total = marks1 + marks2 + marks3 + marks4 + marks5
                total_percentage = (marks1 + marks2 + marks3 + marks4 + marks5)*100/500

                #Condition for grades
                if total_percentage >=90:
                   grade = "A"
                elif total_percentage >=75:
                   grade = "B"
                elif total_percentage >=60:
                    grade = "C"
                elif total_percentage >=40:
                    grade =  "D"
                else :
                    grade = "F"

                

                with open("report.txt","a") as f:
                    report_line = f"student name : {name},\n Total marks : {total},\n Total percentage : {total_percentage},\n Grade : {grade}\n"
                    f.write(report_line)
                    print("To see the report of the student ,please open the 'report.txt' file")
    
    if choose ==3 :
        print("Thank you for visiting")