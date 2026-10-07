#write a program to search for an element in a list and return the index of the element if found, else return -1.

def search_element(list,element):
    for i in range(len(list)):
        if (list[i] == element):
            return i
    return -1

list = []
No_of_elements = int(input("Enter the number of elements in the list: "))
for i in range(No_of_elements):
    elements = int(input("Enter the element :"))
    list.append(elements)

element = int(input("Enter the element to search for: "))
index = search_element(list,element)
if index != -1:
    print(f"The element {element} is found at index {index}.")
else:
    print(f"The element {element} is not found in the list.")
