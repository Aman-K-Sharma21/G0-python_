# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector

class TwoDvector :
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"TwoDvector is : {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The ThreeDvector is : {self.i}i + {self.j}j + {self.k}k")


b = TwoDvector(1,2)
b.show()
a = ThreeDvector(1,2,3)
a.show()