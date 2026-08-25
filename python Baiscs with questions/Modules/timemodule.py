import time

initial = time.time()

k = 0
while(k<45):
    print("This is a number ")
    time.sleep(2)
    k +=1

print("While loop ran in ",time.time() - initial,"seconds")

initial2 = time.time()
for i in range(45):
    print("This is a number")
print("For loops rans in ",time.time() - initial2, "seconds")


#------------------------------------

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

