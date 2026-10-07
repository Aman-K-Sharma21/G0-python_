""" 
Create a function that receives a list of marks and returns:
1.Highest
2.Lowest
3.Average
"""

def Cal_func(list):
    highest = -200
    lowest = 200
    total_marks = 0
    for marks in list:
        if marks > highest:
            highest = marks
        if marks < lowest : 
            lowest = marks
        total_marks +=marks
    average = total_marks/len(list)

    return highest,lowest,average

list = [90,87,99,56,78,88,56,44]
highest,lowest,average = Cal_func(list)

print(f"The highest,lowest and average marks = {highest},{lowest},{average}")
    
