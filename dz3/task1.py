n = [int(x) for x in input()]
yen = False
for i in n:
    if i%2 == 1:
        yen = True
        break
print(yen)