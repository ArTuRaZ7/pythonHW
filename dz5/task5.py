arr = [int(x) for x in input().split()]
co = 0
for i in arr:
    if arr.count(i) > co:
        co = arr.count(i)
print(co)