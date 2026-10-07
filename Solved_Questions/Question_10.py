#Write a program to find all the duplicate elements.

def find_duplicate(arr):
    """This function is used to find the duplicate element in the list"""
    duplicate = []
    seen = set()

    for item in arr:
        if item in seen and item not in duplicate:
            duplicate.append(item)
        else:
            seen.add(item)
    return duplicate

#Example usage

arr = [1,2,3,4,5,6,2,3,4,5,6]
print(f"Duplicates are : {find_duplicate(arr)}")
