# Write a program to Count frequency of every word in a sentence.

sentence = input("Enter a sentence : ")

freq = {}
count = 0
for i in sentence:
    letter = i
    for j in sentence:
        if letter == j:
            count +=1
    freq[letter] = count
    count = 0

print(freq)


