# original array
a = [1,2,4,5,3,4,3,4,6,3,3,2,6,5]
# array store the count of each number
# In this case, 0 ~ 6
# [0, 1, 2, 4, 3, 2, 2]
b = [0] * (max(a)+1)
for i in range(len(a)):
    b[a[i]] += 1

# Modify the count array such that each element
# at each index stores the sum of previous counts.
# [0, 0, 1, 3, 7, 10, 12]
c = [0] * (max(a)+1)
for i in range(1, len(b)):
    c[i] = b[i-1] + c[i-1]

d = [0] * (len(a))
for i in range(len(b)):
    count = b[i]
    start = c[i]
    for j in range(count):
        d[start] = i
        start += 1

print(d)