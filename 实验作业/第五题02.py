def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = int(len(lists)/2)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)
def merge(left, right):
    ri, le = 0, 0
    result = []
    while le < len(left) and ri < len(right):
        if left[le] < right[ri]:
            result.append(left[le])
            le += 1
        else:
            result.append(right[ri])
            ri += 1
    result += left[le:]
    result += right[ri:]
    return result

if __name__=="__main__":
    print(merge_sort([49,38,65,97,76,13,27,49]))










