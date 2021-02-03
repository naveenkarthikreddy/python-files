a=int(input("enter the value of the int1"))
b=int(input("enter the value of the int2"))
c=int(input("enter the value of the int3"))


i=[int(char) for char in str(a)]
j=[int(char) for char in str(b)]
k=[int(char) for char in str(c)]

s1 = i[0] if i[0] < j[0] and i[0] < k[0] else j[0] if j[0]<k[0] else k[0]

s2 = i[1] if i[1] < j[1] and i[1] < k[1] else j[1] if j[1]<k[1] else k[1]

s3 = i[2] if i[2] < j[2] and i[2] < k[2] else j[2] if j[2]<k[2] else k[2]

s4 = i[3] if i[3] < j[3] and i[3] < k[3] else j[3] if j[3]<k[3] else k[3]

k=str(s1)+str(s2)+str(s3)+str(s4)
print(k)