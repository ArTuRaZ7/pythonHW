class Triangle:
    def __init__(self, a, b, c):
        if a<b+c and b<a+c and c<a+b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError('Нельзя составить такой треугольник!')

    def get_squere(self):
        p = (self.a + self.b + self.c)/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

    def get_perimeter(self):
        return self.a + self.b + self.c

tr1 = Triangle(3,4,5)
print(tr1.get_squere())
print(tr1.get_perimeter())