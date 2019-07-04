# @Time    : 4/15 0015 14:41
# @Author  : Lain
def josephus_A(n, k, m):
    people = list(range(1, n+1))

    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end = "")
                people[i] = 0
            i = (i + 1) % n
        if num < n - 1:
            print(", ", end="")
        else:
            print("")
    return

josephus_A(10, 2, 7)