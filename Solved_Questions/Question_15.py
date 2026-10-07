# Determine whether a sentence is a palindrome after ignoring spaces and capitalization.

def palindrome_check(string):
    """This is the function used to check if the given string and it's reversed form is equal or not."""
    #reversed the given string to check with the actual string. 
    rev_string = string[::-1] 

    #Check for equality.
    if(string == rev_string):
        return "True"
    return "False"

given_string = input("Enter the string : ")
print(palindrome_check(given_string))