# list = ["Harry","Larry","Carry","Marie"]

# for item in list:
#     print(item)

#--------------------------------------------

# list = [["Harry",1],["Larry",2],["Carry",6],["Marie",250]]

# for item in list:
#     print(item)

#------------------------------------------

# list = [["Harry",1],["Larry",2],["Carry",6],["Marie",250]]

# for item,chocolate in list:
#     print(item, " and chocolate is ", chocolate)

#-------------------------------------------
# list = [["Harry",1],["Larry",2],["Carry",6],["Marie",250]]

# dict1 = dict(list)
# # print(dict1)

# for item,chocolate in dict1.items():
#     print(item, " and chocolate is ", chocolate)

#--------------------------------------------
# list = [["Harry",1],["Larry",2],["Carry",6],["Marie",250]]

# dict1 = dict(list)
# # print(dict1)

# for item in dict1:
#     print(item)

#-------------------------------------------

#we can use conditional statement inside loops

# .isnumeric is a function used to check and return only numbers;

#-----------X---------X----------------X-------

#while loop

# i = 0
# while(i<45):
#     print(i)
#     i +=1

#----------------------------------------

#break and continue


# i = 0
# while(True):
#     if i<5:
#          i +=1
#          continue
#     print(i, end=" ")
#     if(i == 43):
#         break #stop the loop     
#     i +=1

#--------------------------------------------



while(1):
    num = int(input("Enter a number :"))
    if(num > 100):
        print("You entered a number greater than 100")
        break
    else:
        print("try again")
        continue
    
