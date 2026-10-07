count_dict = {}
string = input("Enter the sentence : ")

list = string.split()

for i in range(len(list)):
    word = list[i]
    count = 0
    for j in range(len(list)):
        if word == list[j]:
            count +=1
        count_dict[word] = count
    count = 0
largest = -1
for name , val in count_dict.items():
    if val > largest:
        largest = val
        which = name

print(f"The most frequent word in the sentence is : {which} which appears {largest} times")


    