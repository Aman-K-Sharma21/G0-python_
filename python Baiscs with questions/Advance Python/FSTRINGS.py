#F Strings
import math
name = "james"
al = 3
a = "this is %s %s"%(me,al)
a = "This is {} {}"
b = a.format(name,al)
print(b)

a = f"this is {name} {al} {4*2} {math.cos(90)}"
print(a)
