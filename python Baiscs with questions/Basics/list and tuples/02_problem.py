# Write a program to accept marks of 6 students and display them in a sorted 
# manner.

marks = []

marks.append(int(input("enter the marks of the first student :")))
marks.append(int(input("enter the marks of the second student :")))
marks.append(int(input("enter the marks of the third student :")))
marks.append(int(input("enter the marks of the fourth student :")))
marks.append(int(input("enter the marks of the fifth student :")))
marks.append(int(input("enter the marks of the sixth student :")))

marks.sort()
print(marks)
