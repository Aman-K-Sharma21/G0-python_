# Function to find the larger of two numbers

def larger(a,v):
    if a > v:
       return a
    else:
        return v



a = int(input("enter the first number :"))
v = int(input("enter the second number :"))

print(f"the larger number is : {larger(a,v)}")