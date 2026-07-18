# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?

class demo:
    a = 4

o = demo()
print(o.a)
o.a = 0
print(o.a)