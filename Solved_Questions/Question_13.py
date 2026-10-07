# Write a program to find students who scored above the class average.

marks = {
    "James" : 98,
    "Clara" : 99,
    "Alex" : 91,
    "Julius" : 92,
    "Robert" : 88,
    "Emily" : 80
}
# highest = marks["James"]
total_marks = 0
for mark in marks.values():
    total_marks +=mark
average = (total_marks)/len(marks)

greater_than_average = []

for student,mark in marks.items():
    if marks[student] >= average:
        greater_than_average.append(student)

print(f"This is the list of students who score >={average:.2f} : {greater_than_average}")



