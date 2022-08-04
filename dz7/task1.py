class Device:
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def get_info(self):
        return f"Device type: {self.type} \nDevice id: {self.id}"


class CoffeeMachine(Device):
    def __init__(self, type, id, specifications):
        self.specifications = specifications
        super().__init__(type, id)

    def get_specifications(self):
        return self.specifications

    def change_specifications(self, specifications):
        self.specifications = specifications


class Blender(Device):
    def __init__(self, type, id, specifications):
        self.specifications = specifications
        super().__init__(type, id)

    def get_specifications(self):
        return self.specifications

    def change_specifications(self, specifications):
        self.specifications = specifications


class MeetGrinder(Device):
    def __init__(self, type, id, specifications):
        self.specifications = specifications
        super().__init__(type, id)

    def get_specifications(self):
        return self.specifications

    def change_specifications(self, specifications):
        self.specifications = specifications


b = Blender("blender", 12345, {"brand": "samsung}", "power": 20})
print(b.get_info())
print(b.get_specifications())