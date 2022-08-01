class Length:
    @staticmethod
    def meters_to_ft():
        m = int(input("Введите количество метров"))
        return m*3.28084

    @staticmethod
    def ft_to_meters():
        ft = int(input("Введите количество футов"))
        return ft*0.3048

print(Length.meters_to_ft())
print(Length.ft_to_meters())