#Write a program to find the average of numbers.

def average_of_numbers(list,numberofelements):
    sum = 0
    for i in range(numberofelements):
        sum += list[i]
    average = sum / numberofelements
    return average

numbers = []

No_of_elements = int(input("Enter the number of elements in the list: "))
for i in range(No_of_elements):
    elements = int(input("Enter the element :"))
    numbers.append(elements)

print(f"The average of the numbers you entered is : {average_of_numbers(numbers,No_of_elements)}")

