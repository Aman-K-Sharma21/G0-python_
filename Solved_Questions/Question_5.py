# Write a program to reverse a list without using the reverse() function.

def reverse_list(list):
    reversed_list = []

    for i in range(len(list)):
        reversed_list.append(list[::-1][i])
    return reversed_list

list = [1,2,3,4,5,6]
print(f"The reversed list is : {reverse_list(list)}")