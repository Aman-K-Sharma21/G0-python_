# Classes - Template
# Object - Instance of the class

# DRY - Do Not repeat yourself

# class student:
#     pass

# james = student()
# jack = student()

# james.name = "James"
# james.std = 9
# james.section = 1

# print(james.name , james.section)

#----------------------------------------------

# class Employee:
#     no_of_leaves = 8
    
# james = Employee() #instance 1
# jack = Employee() #instance 2

# james.name = "james"
# james.salary = 200
# james.role = "Guide"

# jack.name = "Jack"
# jack.salary = 300
# jack.role = "traveller"
# #we can access the instance variable of james and jack using james and jack.

# print(Employee.no_of_leaves)
# print(jack.__dict__)
# james.no_of_leaves = 9# we cannot class attribute by uisng object.
# print(Employee.no_of_leaves)

#we cannot change the class attribute using instance object but we can access the class attribute using instance object 

#------------------------------------------------------------------------------

# class Employee:
#     no_of_leaves = 8
#     def printdetails(self): #methods
#         return f"Name is {self.name} . Salary is {self.salary} and role is {self.role}"

# james = Employee() #instance 1
# jack = Employee() #instance 2

# james.name = "james"
# james.salary = 200
# james.role = "Guide"

# jack.name = "Jack"
# jack.salary = 300
# jack.role = "traveller"
# #we can access the instance variable of james and jack using james and jack.

# print(Employee.no_of_leaves)
# print(jack.__dict__)
# james.no_of_leaves = 9# we cannot modify class attribute by uisng object.
# print(Employee.no_of_leaves) #we cannot change the class attribute using instance object but we can access the class attribute using instance object 



# print(james.printdetails())
# print(jack.printdetails())

#-------------------------------------------------------------------------

##constructor

# --> after creating class , we create object of class and then object attribute/variable like this ,

# class Employee:
#     no_of_leaves = 8
#     def printdetails(self): #methods
#         return f"Name is {self.name} . Salary is {self.salary} and role is {self.role}"

# james = Employee() #instance 1
# jack = Employee() #instance 2

# james.name = "james"
# james.salary = 200
# james.role = "Guide"



# but isn't it would be more to assign object variable value while creating object.

# so, constructor is the way to give arguement to the class
# class Employee():

#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

# james = Employee("james",4444,"Guide") # when i give argument to the class while creating object , it always handeled by init function

#-------------------------------------------------

# class Employee():
#     no_of_leaves = 9

#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"The Name is {self.name} and the salary is {self.salary} and the role is {self.role}"

#     @classmethod
#     def change_leaves(cls,newleaves):
#         cls.no_of_leaves = newleaves


# james = Employee("james",333,"Guide")
# jack = Employee("jack",333,"charisma")

# james.change_leaves(55)

# print(jack.no_of_leaves)

#--------------------------------------------------------

# class Employee():
#     no_of_leaves = 9

#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"The Name is {self.name} and the salary is {self.salary} and the role is {self.role}"

#     @classmethod
#     def change_leaves(cls,newleaves):
#         cls.no_of_leaves = newleaves
#     @classmethod
#     def from_dash(cls,string):
#         # juli = string.split("-")
#         # print(juli)
#         # return cls(juli[0],juli[1],juli[2])
#         #but wha if i want to do the same things but in one line not three line, we use the concept of args and kwargs
#         return cls(*string.split("-"))


# james = Employee("james",333,"Guide")
# jack = Employee("jack",333,"charisma")
# yo = Employee.from_dash("yo-33-gamer")

# james.change_leaves(55)

# print(jack.no_of_leaves)


#-------------------------------------------------------------------------------

# @staticmethod
# def printgood(string):
#     print("This is good" + string)

# Employee.printgood("seno")
# or 
# printgood("seno")

#------------------------------------------------------

#Abstraction & encapsulation

# abstraction means breaking a work into smaller piece
# In order to achieve abstraction in OOPS in python , we have to do encapsulation.

# encapsulation means hiding the details
        
# aam khae ghutli na gine. for example , you type the letter in keyboard and it will display in the screen ,you type the keyboard and letter appears in the screen that's it , Now, it do that i don't care how but it does.

#--------------------------------------------------------

#-----------------------INHERITANCE---------------------------
# class programmer(Employee):
#     no_of_holiday = 56

#     def __init__(self,aname,asalary,arole,language):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.language = language
    
#     def printprog(self):
#         return f"The Programmer's Name is {self.aname} and salary is {self.asalary} and the role is {self.role}"

# synape = Employee("synape",233,"instructor")
# ron = Employee("ron",555,"student")

# grenjoy = programmer("grey",454,"programmer",["python"])
# print(grenjoy.no_of_holiday)


#--------------MULTIPLE INHERITANCE--------------

class Employee:
    no_of_leaves = 8

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    def printdetails(self):
        return f"The name is {self.name}.The salary of the employee is {self.salary} and the role is {self.role}"
    
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good" + string)

class Player:
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f"The name of the player is {self.name}. The name of the game is {self.game}"

class CoolProgrammer(Player,Employee):
    language = "c++"
    def printlanguage(self):
        print(self.language)

jackie = Employee("jackie",45000,"webdev")
perma = Player("perma",["Cricket"])
# tichala = CoolProgrammer("tichala",56000,"coolprogrammer")
tichala = CoolProgrammer("tichala",["wrestling"])
dot = tichala.printdetails()
print(dot)


