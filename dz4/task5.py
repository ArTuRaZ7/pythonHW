n = int(input())
s = 0
for i in range(1,n+1):
    s+=1/((2*i)**2)
print(round(s, 6))