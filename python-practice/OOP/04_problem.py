# Add a static method in problem 2, to greet the user with hello. 


class calculator :
    def __init__(self,n):
        self.n = n

    def square(self) :
        print(f"the square of the number is : {self.n*self.n}")

    def cube(self) :
        print(f"the cube of the number is : {self.n*self.n*self.n}")

    def square_root(self) :
        print(f"the square root of the number is : {self.n**(1/2)}")

    @staticmethod
    def greet():
        print("Hello")


b = int(input("enter the number : "))
a = calculator(b)
a.square()
a.cube()
a.square_root()
a.greet()