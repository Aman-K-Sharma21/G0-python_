# def function1():
#     print("Subscribe now")
# func2 = function1 # copy of function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int

# a = funcret(1)
# print(a)

# def executer(func):
#     func("This")
# executer(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def goat_plays():
    print("Ronaldo")
# goat_plays = dec1(goat_plays)
goat_plays()