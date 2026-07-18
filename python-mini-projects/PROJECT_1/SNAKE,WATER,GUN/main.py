"""
1 for snake 
-1 for water
0 for gun

"""

import random

computer = random.choice([1,-1,0])

ichoose = input("enter your choice :")
dict = {"s": 1, "w": -1,"g":0}
reversedict = {1:"s", -1:"w",0:"g"}

youchoose = dict[ichoose]

print("computer chose : ",reversedict[computer])
print("you chose : ",reversedict[youchoose])
if computer == youchoose:
    print("tie")
else:
    if(computer ==1 and youchoose ==-1): #computer -youchoose = 2
        print("you loose")
    elif(computer ==1 and youchoose == 0): #computer -youchoose = 1
        print("you win")
    elif(computer ==-1 and youchoose ==1): #computer -youchoose = -2
        print("you win")
    elif(computer ==-1 and youchoose ==0): #computer -youchoose = -1
        print("you loose")
    elif(computer ==0 and youchoose ==1): #computer -youchoose = 1
        print("you loose")
    elif(computer ==0 and youchoose ==-1): #computer -youchoose = -1
        print("you win")
    else:
        print("invalid input")