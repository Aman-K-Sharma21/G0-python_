# def function_nameprint(a,b,c,d):
#     print(a,b,c,d)

# function_nameprint("james","jerob","ginny","hermonie")

# what if i have to add another name , to do that i have to add another variable which is not efficient.

def funarg(normal,*args, **kwargsshow):
    print(type(args))
    print(normal)
    # print(args[0])
    for item in args:
        print(item)
    for key,value in kwargsshow.items():
        print(f"{key} is a {value}")

names = ["james","jerob","ginny","hermonie","jack"]
normal = "I am a normal arugement and the students are :"
kw = {"Rohan":"Monitor","Akash":"cook","julius":"Assistant","vir":"instructor"}
funarg(normal,*names,**kw)