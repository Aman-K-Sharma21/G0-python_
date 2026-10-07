#Write a program to find the count frequency of every number in a list.


# list = [1,2,3,4,5,1,2,3,4]

# freq = {}
# for i in range(len(list)):
#     number = list[i]
#     count = list.count(number)
#     freq[number] = count

# print(freq)
    

#------------------------------------------

list = [1,2,3,4,5,1,2,3,4]

freq = {}
count = 0
for i in range(len(list)):
    number = list[i]
    for j in range(len(list)):
        if number == list[j]:
            count +=1
            freq[number] = count
    count = 0

print(freq)





