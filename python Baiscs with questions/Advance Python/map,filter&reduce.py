###MAP


# number = ["3","44","64"]

# for item in range(len(number)):
#     number[item] = int(number[item])

# numbers = list(map(int,number))

# number[2] = number[2] +1
# print(number[2])

#-----------------------------------

# num = [2,3,4,5,6,7,4,5,55,22]

# square = list(map(lambda x:x*x , num))

# print(square)

#------------------------------------

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a

# func = [square,cube]

# for i in range(5):
#     val = list(map(lambda x:x(i) , func))
#     print(val)

#----------------------------------

###FILTER

# list1 = [1,2,3,4,5,6,7]

# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5,list1))
# print(gr_than_5)

#-----------------------------------

###REDUCE

from functools import reduce

list1 = [1,2,3,4]
# num = 0

# for i in list1:
#     num +=i
num = reduce(lambda x,y:x+y , list1)
num1 = reduce(lambda x,y:x*y , list1)
print(num)
print(num1)