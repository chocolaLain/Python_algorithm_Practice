import time

def insertionSort(arr): 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
    return arr


if __name__ == '__main__':

    array = [30, 13, 25, 16, 27, 19, 10]
    instert_after = insertionSort(array)
    print(instert_after)




