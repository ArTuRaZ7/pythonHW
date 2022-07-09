a = int(input())
b = int(input())
n = int(input())
s = (a+b*0.01)*n
print(int(s//1), int((s%1)*100))