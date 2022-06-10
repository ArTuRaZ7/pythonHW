arr = [int(x) for x in input().split()]
m = abs(arr[0]-arr[1])
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        if abs(arr[i]-arr[j]) < m:
            m = abs(arr[i]-arr[j])
print(m)