# Write a program to make a copy of a text file “this. txt”

with open("this.txt") as f:
    a = f.read()
with open("this_copy_text.txt","w") as f:
    f.write(a)