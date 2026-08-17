# # list

# series = ["BB","GOT","HP","LOR","AIB",33]

# print(series[0])
# print(series[1])

# numbers = [2,4,7,9,11,3]
# print(numbers[1])
# # numbers.sort()
# # numbers.reverse()
# print(numbers[2])

# #list slicing

# print(numbers[:5]) #slicing return a new list but .sort(),.reverse() methods change the original lists.

# print(numbers[::-1]) # reverse the list , don't take the step lower than -1 because if you write -2 or -3 , it first reverse the list then perform the task which is not generally considered.

# print(len(numbers))
# print(max(numbers))
# print(min(numbers))

# numbers.append(8)

# numbers.insert(2,67)

# numbers.remove(9)

# numbers.pop()

# numbers[1] = 99
# print(numbers)



#---------------------------------------

# Mutable - can change , eg:-list
#Immutable - cannot change , eg:-tuple

#--------------------------

# tuple
# tup = (1,) #single element tuple
# tp = (1,2,3) #Multiple element tuples.
# print(tp)
# print(type(tp))

# tp[0] = 2 # tuples are immutable , it's value at particular index cannot be changed.
# print(tp)

# a = 1
# b = 8

# a , b = b , a #swap

# print(a)
# print(b)
# print(a,b)
