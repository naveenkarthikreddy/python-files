from functools import reduce
x = int(input("enter the value of x"))
y = int(input("enter the value of y"))
z = int(input("enter the value of z"))
n = int(input("enter the calue of n"))
lister = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            localLister = [i, j, k]
            lister.append(localLister)
listerr=[]         

for l in lister:
    print(l)

    result = reduce((lambda a, b: a + b), l)
    print(result)
    if (result != n):
        print(lister)
        listerr.append(l)
        print(lister)
print(listerr)
