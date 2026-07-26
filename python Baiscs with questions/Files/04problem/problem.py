with open("log.txt") as f:
    contents = f.readlines()
lineno = 1
for content in contents:
    if "python" in content:
        print(f"yes, python is in the line : {lineno}")
        break
    lineno +=1
else:
    print("No,python is not in the para")
    