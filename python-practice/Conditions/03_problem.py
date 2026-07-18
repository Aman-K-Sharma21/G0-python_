# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

text= input("enter the text :")

p1 = "make a lot of money"
p2 = "buy now" 
p3 = "subscribe this"
p4 = "click this"

if (p1 in text) or (p2 in text) or (p3 in text) or (p4 in text) :
    print("spam detected")
else :
    print("good to go not a spam")

