#  Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint

class Train :

    def __init__(slf,trainNo):
        slf.trainNo = trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")
    def getStatus(slf,trainNo) :
        print(f"Ticket no : {slf.trainNo} is running on time")
    def getFare(slf,fro,to) :
        print(f"Ticket fare in train no : {slf.trainNo} from {fro} to {to} is {randint(150,500)}")

t = Train(15737)
t.book("kashmir","chennai")