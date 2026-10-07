# Write a program to Find the student with the highest marks from a dictionary.

""" There was a science test two days ago, the result will announce tommorrow 
. So we have to write a program to find the student with the highest marks."""

marks = {
    "James" : 98,
    "Clara" : 99,
    "Alex" : 91,
    "Julius" : 92,
    "Robert" : 88,
    "Emily" : 80
}
highest = marks["James"]

for name,mark in marks.items():
    if marks[name] > highest:
        highest = marks[name]
        person = name

print(f"The student who got the highest marks is {person} which is {marks[person]}")





