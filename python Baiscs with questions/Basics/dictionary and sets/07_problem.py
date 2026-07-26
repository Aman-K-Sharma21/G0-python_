# If the names of 2 friends are same; what will happen to the program in problem 
# 6? 

#answer to this question is that if the names of 2 friends are same then the program will overwrite the previous value of the key with the new value, so we will lose the previous value of the key.
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