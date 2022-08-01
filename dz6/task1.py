class Fraction:

    count = 0

    def set_data(self):
        Fraction.count += 1
        num = int(input('Введите числитель:\t'))
        denom = int(input('Введите знаменатель:\t'))
        self.num, self.denom = Fraction.reduce(num, denom)

    def reduce(num, denom):
        for i in range(2, min(num, denom)):
            while num % i == 0 and denom % i == 0:
                num //= i
                denom //= i
        return num, denom



    def print_info(self):
        print(f'{self.num} / {self.denom}')


    def get_frac(self):
        return self.num, self.denom

    @staticmethod
    def get_count():
        return Fraction.count

f = Fraction()
f.set_data()
f.set_data()
f.print_info()
print(f.get_frac())
print(Fraction.get_count())