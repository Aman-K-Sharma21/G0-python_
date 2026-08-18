mystr = "Silent Hill 2 is the beautiful game"
print(mystr)
print(mystr[2]) #l
print(mystr[0:2]) #Si # 0 is including but 2 is excluding

print(len(mystr)) # 36
print(mystr[0:35])
# print(mystr[76]) # error --> index out of range

print(mystr[0:55]) #if the end index is greater than the string end index then it prints the whole string and give it.

#advanced slicing

print(mystr[0:5:2]) #sln

print(mystr[:6]) #if the starting index is not given then by default it takes 0. similarly if the ending index is not given , it takes the whole length of the string.

print(mystr[0:])


print(mystr.isalnum()) #alphanumeric means it have to only contain alphabet or number to be true no spaces,symbols,punctions.

print(mystr.isalpha) # to be true it should only contain only alphabets no spaces,numbers,symbols and punctions.

print(mystr.endswith("game"))

print(mystr.count("i"))
print(mystr.capitalize()) #to capitalize the first letter of the string

print(mystr.upper()) #lower every single character in the string
print(mystr.lower()) # upper every single character in the string

print(mystr.replace("is","are"))

# for more search online