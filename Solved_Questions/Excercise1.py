student = {
    "name": "Alex",
    "age": 18,
    "marks": {
        "python": 85,
        "math": 78,
        "english": 82
    }
}

#write code that calculates the student's total and average.
"""
Method-1

# total_marks = sum(student["marks"].values())
# average_marks = total_marks / len(student["marks"])
"""

"""Method-2"""
total_subject = 0
total_marks = 0
for marks in student["marks"].values():
    total_marks +=marks
    total_subject +=1

average_marks = total_marks / total_subject
print(f"Total Marks : {total_marks} and Average Marks : {average_marks:.2f}")
