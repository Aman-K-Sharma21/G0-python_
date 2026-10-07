# Create a student dictionary and search for a student by name.

"""
Result of science test are to be declared. The highest marks that a student can get is 50.
"""

student_dict = {"james" : 48,"julius" : 49,"jarvis" : 50,"alex" : 45}

#Student list :
for name in student_dict.keys():
    print(name)

Name = input("Enter the name of student to see the marks of the test : ").lower()
print(student_dict[Name])