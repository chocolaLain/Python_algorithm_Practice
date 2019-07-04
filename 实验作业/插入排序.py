lst = [35, 23, 26, 42, 18, 28, 37, 45]
#print(insert_sort(lst))

def insertSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            j -= 1
    return arr
print(insertSort(lst))
