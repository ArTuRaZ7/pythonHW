arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
res = []
for i in arr1:
    if i in arr2:
        res.append(i)
if len(res) == 0:
    print(-1)
print(*res)