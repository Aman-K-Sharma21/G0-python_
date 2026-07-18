#A multiplication table genertor from the any number to any number. For example : 2 to 10, 5,20 etc

def tablegen(n):
    table = ""

    for i in range(1,11):
        table += f"{n} X {i} = {n*i} \n"
    with open(f"table/tableof{n}.txt","w") as f :
        f.write(table)


a =int(input("you want the multiplication table from the number :"))
b = int(input("you want the multiplication table till the number + 1 :"))
for i in range(a,b):
    tablegen(i)


    