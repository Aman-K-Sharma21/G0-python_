#  Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50  => F 

m = int(input("enter the marks :"))

if m <=100 and m >=90 :
    grade = "Ex" 
elif m <90 and m>=80 :
    grade = "A"
elif m <80 and m>=70:
    grade = "B"
elif m<70 and m>=60 :
    grade = "C"
elif m <60 and m >=50 :
    grade = "D"
elif m <50 :
    grade = "F"

print("your grade is", grade )
