a = [65, 12, 46, 97, 56, 33, 75, 53, 21]

def q_sort(l:list, left:int, right:int):
    if left >= right:
        return l
    n = len(l)
    i = left
    j = right
    x = l[(i + j)//2]

    while i <= j:
        while l[i] < x:
            i += 1
        while l[j] > x:
            j -= 1
        if i <= j:
            t = l[i]
            l[i] = l[j]
            l[j] = t
            i += 1
            j -= 1

    q_sort(l, left, j)
    q_sort(l, i, right)

q_sort(a, 0, 8)
for i in range(len(a)):
    print(a[i])

