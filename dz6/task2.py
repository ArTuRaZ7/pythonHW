class Temperature:
    count = 0
    @staticmethod
    def celsium_to_farengeit():
        Temperature.count +=1
        degrees = int(input("Введите количество градусов по Цельсию"))
        return degrees*9/5+32

    @staticmethod
    def farengeit_to_celsium():
        Temperature.count += 1
        degrees = int(input("Введите количество градусов по Фаренгейту"))
        return (degrees-32)*5/9

    @staticmethod
    def get_count():
        return Temperature.count

print(Temperature.farengeit_to_celsium())
print(Temperature.celsium_to_farengeit())
print(Temperature.get_count())