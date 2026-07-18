#  Write a python program using function to convert Celsius to Fahrenheit. 

def ctf(c):
    f =(c*9/5)+32
    return f

c = float(input("enter the temperature in celsius :"))

print(f"the temperature in fahrenheit is : {ctf(c)}")