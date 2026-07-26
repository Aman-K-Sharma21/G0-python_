#  Write a program to find out whether a given post is talking about “Harry” or not. 

post = input("Enter the post :")

if "harry" in post.lower() :
    print("this poster is talking about harry")
else :
    print("this poster is not talking about harry")