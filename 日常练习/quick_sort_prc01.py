def quick_sort(alist):
    quick_rec(alist, 0, len(alist)-1)

def quick_rec(alist, start, end):
    if start >= end:
        return
    low = start 
    high = end
    mid = alist[start]

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] <= mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid
    quick_rec(alist, start, low-1)
    quick_rec(alist, low+1, end)

if __name__ == '__main__':
    alist = [11, 4, 6, 3,7, 2, 10 ,6]
    quick_sort(alist)
    print(alist)
