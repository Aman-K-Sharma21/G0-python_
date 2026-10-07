#Write a program to count the number of even and odd numbers in a list.

def count_even_odd(list):

    even_count = 0
    odd_count = 0

    for i in range(len(list)):
        if (list[i] % 2 == 0):
            even_count +=1
        else:
            odd_count +=1
    return f"The number of even numbers in the list is : {even_count} and the number of odd numbers in the list is : {odd_count}"

list = []

No_of_elements = int(input("Enter the number of elements in the list: "))
for i in range(No_of_elements):
    elements = int(input("Enter the element :"))
    list.append(elements)

print(f"{count_even_odd(list)}")
