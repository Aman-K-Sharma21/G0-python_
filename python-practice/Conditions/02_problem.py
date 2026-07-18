#  Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

marks1 = int(input("enter the marks of first subject :"))
marks2 = int(input("enter the marks of second subject :"))
marks3 = int(input("enter the marks of third subject :"))

total_marks = marks1 + marks2 + marks3
percentage = total_marks /3

print("total marks is :",total_marks)
print("your percentage is :",percentage)


if (percentage >=40) and (marks1 >=33) and (marks2 >=33) and (marks3 >=33 ):
    print("Congratulations! You have passed the exam.")
else :
    print("sorry! you have failed the exam. Try next year")
