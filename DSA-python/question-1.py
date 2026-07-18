#pattern

"""
1234.....n
1234.....n
1234.....n
1234.....n
....
....
....
nnnn
"""

number = int(input("Enter a number : "))

for i in range(0,number):
    for j in range(0,number):
        print("*",end=" ")
    print("")