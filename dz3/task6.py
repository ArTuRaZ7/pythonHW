n = int(input())
f1 = 1
f2 = 1
f = 2
while f<n:
    f1 = f2
    f2 = f
    f = f1+f2
if f == n:
    print(True)
else:
    print(False)