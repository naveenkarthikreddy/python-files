a = eval(input("enter the first set of vaues"))
b = eval(input("enter the second set of vaues"))
ucl = []
l1 = len(a)
l2 = len(b)
for i in a:
    if i not in b:
        ucl.append(i)   
for i in b:
    if i not in a:
        ucl.append(i)   
print(ucl)
sum=0
for i in ucl:
    sum=sum+i
print(sum)    
sum_str=str(sum)

while(len(sum_str)!=1):
    fO=0
    for i in range(len(sum_str)):
        fO=fO+int(sum_str[i])
    sum_str=str(fO)    
print(fO)        