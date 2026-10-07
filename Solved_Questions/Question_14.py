"""
Count the frequency of each character in a string.
Example : apple

a --> 1
p -->2
l --> 1
e --> 1
"""

string = input("Enter the string : ")

count_char = {}

for i in range(len(string)):
    char_check = string[i]
    count = 0
    for j in range(len(string)):
        if char_check == string[j]:
            count +=1
        count_char[char_check] = count
    count = 0

print(count_char)




