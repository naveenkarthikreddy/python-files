def linearSearch(my_array, target):
    j = 0
    for i in range(len(my_array)):
        if(my_array[i] == target):
            j = j+1
            return i
    print(j)
    return -1

 
# print(linearSearch([5,3,2,4,5,6],2))
k = 4
for i in range(5):
    k = k+1
print(k)
