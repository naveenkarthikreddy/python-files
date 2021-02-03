a=eval(input("enter the value of the first list"))
b=eval(input("enter the value of the second list"))
l1=len(a)
l2=len(b)
lister=[]

for i in a:
    k=0
    for j in b:
        k=k+1
        print(k)
        if(i==j):
            break
        if(k==l2):
            lister.append(i)

for i in b:
    k=0
    for j in a:
        k=k+1
        print(k)
        if(i==j):
            break
        if(k==l1):
            lister.append(i)

print(lister)
