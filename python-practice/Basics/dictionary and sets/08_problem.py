# If languages of two friends are same; what will happen to the program in problem 
# 6? 
#answer to this question is that values of the keys can be same but keys cannot be because keys are identifiers and they have to be unique

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