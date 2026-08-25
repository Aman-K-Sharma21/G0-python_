# file Input/Output

# Ram is volatile and ROM is non-volatile

""" 
"r" - Open file for reading - default
"w" - Open a file for writing
"x" - creates file if not exists
"a" - Add more content to a file
"t" - Text mode (eg:-python file,text file , etc) - default
"b" - binary mode
"+" - read and write
"""

f = open("theory.txt","rt")
# content = f.read()
# content = f.read(3) #read three characters

for line in f: # to read one line at a time.
    print(line, end="")

print(f.readline) # do the same thing but each readline gives only one line

print(f.readlines) #gives all lines in a list
# print(content)
f.close()

#---------------------------------------------

# f = open("theory.txt","a")
# a = f.write("Theory is for revision") 
# print(a) # prints the number of character its write.
# f.close()

#--------------------------------------

# f = open("theory.txt","w")
# a = f.write("Theory is for revision") 
# print(a) # prints the number of character its write.
# f.close()

#--------------------------------------
#handle read and write both

# f = open("theory.txt","r+")
# print(f.read())
# f.write("thank you")
# f.close()

#--------------------------------------

# f = open("theory.txt")
# print(f.tell()) # tells where is our file pointer
# print(f.readline())
# print(f.tell()) 
# f.seek(0) # reset the file pointer to starting position
# f.close()

#------------------------------------------

# with open("theory.txt") as f:
#     a = f.read(4)
#     print(a)