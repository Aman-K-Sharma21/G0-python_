# Write a program to Sort numbers without using sorted() or .sort() on a list — try your own logic.


list = [34,32,55,43,23,6,2,1,4]

nlist = []

for i in range(len(list)):
    for j in range(len(list)):
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]

print(f"The sorted list is : {list}")