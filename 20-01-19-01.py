def buble(arr):
    for itr in range(len(arr)-1):
        for i in range(len(arr)-1-itr):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                print(arr)



arr=[558,23,12,43,23,432,234,553,1]
buble(arr)



