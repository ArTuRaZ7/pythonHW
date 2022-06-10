ab = [float(x) for x in input().split()]
n = int(ab[1])
a = ab[0]
s = 1
for i in range(1, n+1):
    s += ((-1)*a)**i
print(round(s, 3))