arr = [int(x) for x in input().split()]
for j in arr:
    kf = 9999
    ind = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == j:
            continue
        if abs(j - arr[i])<kf:
            kf = abs(j - arr[i])
            ind = i
    print(arr[ind], end=" ")