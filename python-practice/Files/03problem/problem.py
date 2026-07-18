# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.

def rep():
    word = "Donkey"

    with open("file.txt","r") as f:
        content = f.read()

        contentnew = content.replace("Donkey","######")
    with open("file.txt","w") as f:
        f.write(contentnew)


rep()