n = int(input())
s = 0

def fa(x):
    su = 1
    for i in range(1, x+1):
        su*=i
    return su

def de(x):
    su = 0
    for i in range(1,x+1):
        su+=1/(i+1)
    return su

for i in range(1, n+1):
    s += fa(i)/de(i)

print(round(s,6))