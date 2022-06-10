import math as ma
n = int(input("Введите количество точек"))
arr = [tuple((input().split())) for i in range(n)]
m = 99999999999999999999999999999999999999999
mco = [0, 0, 0]
for i in arr:
    for j in arr:
        for k in arr:
            if i == j or i == k or j == k:
                continue
            a = ma.sqrt((int(i[0]) - int(j[0])) ** 2 + (int(i[1]) - int(j[1])) ** 2)
            b = ma.sqrt((int(i[0]) - int(k[0])) ** 2 + (int(i[1]) - int(k[1])) ** 2)
            c = ma.sqrt((int(k[0]) - int(j[0])) ** 2 + (int(k[1]) - int(j[1])) ** 2)
            if a > b+c or b > a+c or c > a+b:
                continue
            p = (a+b+c)/2
            if ma.sqrt(p*(p-a)*(p-b)*(p-c)) < m:
                m = ma.sqrt(p*(p-a)*(p-b)*(p-c))
                mco[0], mco[1], mco[2] = i, j, k

print(f'Минимальная площадь: {m} Точки треугольника с минимальной площадью: {mco}')
