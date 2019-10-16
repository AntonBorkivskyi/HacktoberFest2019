def insertionSort(lst): 

    for i in range(1, len(lst)):
        value = lst[i] 
        j = i-1
        while j >= 0 and value < lst[j] : 
                lst[j + 1] = lst[j] 
                j -= 1
        lst[j + 1] = value 

arr = [22, 21, 23, 15, 16] 
insertionSort(lst) 
for i in lst: 
    print(i)
