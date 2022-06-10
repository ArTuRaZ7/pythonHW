ab = [int(x) for x in input().split()]
a = ab[0]
b = ab[1]
s = 0
for i in range(a,b+1):
    s+=i**2
print(s)