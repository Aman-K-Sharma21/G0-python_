# Can we have a set with 18 (int) and '18' (str) as a value in it? 
#yes

a = set()

b = int(input("enter the number 1 :"))
a.add(b)

c = input("enter the number 2 :")
a.add(c)

print(a) #{18,'18'}

    