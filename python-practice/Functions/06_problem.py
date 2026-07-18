# Write a python function which converts inches to cms.

"""
cm = inches *2.54
"""


def itc(n):
    return n*2.54

n = float(input('enter the number in inches :'))
print(f"the number in cm is : {itc(n)}")