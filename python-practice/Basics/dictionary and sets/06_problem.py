# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

favlang = {}

name1 = input("enter friends name :")
lang1 = input("enter their favourite language :")
favlang.update({name1 : lang1})

name2 = input("enter friends name :")
lang2 = input("enter their favourite language :")
favlang.update({name2 : lang2})

name3 = input("enter friends name :")
lang3 = input("enter their favourite language :")
favlang.update({name3 : lang3})

name4 = input("enter friends name :")
lang4 = input("enter their favourite language :")
favlang.update({name4 : lang4})

print(favlang)