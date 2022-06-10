x = float(input())
arr = [int(x) for x in input().split()]
sr = abs(arr[0]-arr[1])
kf = abs(sr - x)
for i in arr:
    for j in arr:
        if i == j:
            continue
        if abs(abs(i-j)-x) < kf:
            sr = abs(i-j)
            kf = abs(sr - x)
        elif kf == abs(abs(i-j)-x) and sr > abs(i-j):
            sr = abs(i - j)
print(round(sr, 6))