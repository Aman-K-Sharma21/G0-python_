# write a program to remove the duplicate elements from a list and return the new list without duplicates.

def remove_duplicates(list):
    nlist = []
    for i in list:
        if i not in nlist:
            nlist.append(i)
    return nlist

list = [2,3,4,5,2,3,4,5]

print(f"The new list after removing the duplicates is : {remove_duplicates(list)}")

