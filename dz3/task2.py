p = float(input())
s = 10
su = 10
k = 1
while su <= 200:
    s *= (1+p*0.01)
    su += s
    k+=1
print(k, round(su, 6))
