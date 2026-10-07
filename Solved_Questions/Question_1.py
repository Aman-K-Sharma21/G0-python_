#Write a Python program to find the largest,smallest and second largest number in the list without using max() and min() function.

numbers = []

No_of_elements = int(input("Enter the number of elements in the list: "))
for i in range(No_of_elements):
    elements = int(input("Enter the element :"))
    numbers.append(elements)

largest = numbers[0]
smallest = numbers[0]

for i in range(len(numbers)):
    if (numbers[i] > largest):
        second_largest = largest
        largest = numbers[i]
    if (numbers[i] < smallest):
        smallest = numbers[i]

print(f"The largest number = {largest} ")
print(f"The smallest number = {smallest}")
print(f"Second largest number = {second_largest}")



