# Function to check even/odd

def even_odd(a):
    if a%2 ==0:
        return "even"
    else:
        return 'odd'
    

a = int(input("enter the number :"))

print(f"{a} is {even_odd(a)}")