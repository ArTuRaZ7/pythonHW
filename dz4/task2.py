ab = [int(x) for x in input().split()]
a = ab[0]
b = ab[1]
arr = []
for i in range(b-1, a, -1):
    arr.append(i)
print(len(arr))
print(*arr)