class Money:
    def set_amount(self):
        self.units = int(input("Введите количество целых"))
        self.penny = int(input("Введите количество копеек"))
        if self.penny >=100:
            self.units += self.penny//100
            self.penny = self.penny%100

    def get_sum(self):
        return f"{self.units}.{self.penny}"
usd = Money()
usd.set_amount()
print(usd.get_sum())