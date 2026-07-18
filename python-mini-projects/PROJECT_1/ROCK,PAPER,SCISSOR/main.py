"""
rock = 1
paper = 2
scissor = 3

"""

import random

computer = random.choice([1,2,3])

ichoose = input("Enter your choice :")
dict = {"rock" : 1,"paper" : 2,"scissor" : 3}
redict = {1 : "rock", 2 : "paper", 3 : "scissor"}


youchoose = dict[ichoose]
print("you chose :",redict[youchoose])
print("computer chose :",redict[computer])



if computer == ichoose:
    print("Its a tie")
elif computer == 1 and youchoose ==2:
    print("you win")
elif computer == 1 and youchoose ==3:
    print("you lose")
elif computer == 2 and youchoose ==1:
    print("you lose")
elif computer == 2 and youchoose ==3:
    print("you win")
elif computer == 3 and youchoose ==1:
    print("you win")
elif computer == 3 and youchoose ==2:
    print("you lose")
else:
    print("Please choose a valid input")

