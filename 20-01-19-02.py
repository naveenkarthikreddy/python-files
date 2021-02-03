def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[min]>arr[j]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]

    print(arr)

arr=[558,23,12,43,23,432,234,553,1]
selectionSort(arr)
