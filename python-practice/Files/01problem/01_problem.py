#  Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

with open("poem.txt","r") as f:
    a = f.read()
    
    if ("twinkle" in a):
        print("your given word is in the text poem.txt file")
    else:
        print("your given word is not in  the poem.txt file")



