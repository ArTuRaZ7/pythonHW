class Ship:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def get_info(self):
        return f"Ship type: {self.type} \nShip name: {self.name}"


class Frigate(Ship):
    def __init__(self, type, name, specifications):
        self.specifications = specifications
        super().__init__(type, name)

    def get_specifications(self):
        return self.specifications

    def change_specifications(self, specifications):
        self.specifications = specifications


class Destroyer(Ship):
    def __init__(self, type, name, specifications):
        self.specifications = specifications
        super().__init__(type, name)

    def get_specifications(self):
        return self.specifications

    def change_specifications(self, specifications):
        self.specifications = specifications


class Cruiser(Ship):
    def __init__(self, type, name, specifications):
        self.specifications = specifications
        super().__init__(type, name)

    def get_specifications(self):
        return self.specifications

    def change_specifications(self, specifications):
        self.specifications = specifications


c = Cruiser("cruiser", "aurura", {"speed":30, "weight":40})
print(c.get_info())
print(c.get_specifications())