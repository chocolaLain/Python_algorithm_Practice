def quick_sort(lst):
        def qsort_rec(lst, l, r):
            if l >= r:
                return
            i = 1
            j = r
            pivot = lst[i]
            while i < j:
                while i < j and lst[j].key >= pivot.key:
                    j -= 1
                if i < j:
                    lst[i] = lst[j]
                    i += 1
                while i < j and lst[i].key <= pivot.key:
                    i += 1
                if i < j:
                    lst[j] = lst[i]
                    j -= 1
                lst[i] = pivot
                qsort_rec(lst, 1, i-1)
                qsort_rec(lst, i+1, r)

        qsort_rec(lst, 0, len(lst)-1)

a = [1, 3, 5, 2, 0, 3, 12, 6]
quick_sort(a)
print