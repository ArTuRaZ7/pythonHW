q = int(input())
i = 0
s = 0
while q >= 1:
    i += 1
    r = q % 10
    s += r
    q = int(q/10)
print(i, s)
