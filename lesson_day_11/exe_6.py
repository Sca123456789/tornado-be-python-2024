class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def introduce(self):
        print(f"Our restaurant name is {self.restaurant_name}. and we serve {self.cuisine_type}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, "Ice Cream")
        self.flavors = flavors

    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)

info = IceCreamStand("Ice Cream Stand", ["Vanilla", "Chocolate", "Strawberry"])
info.introduce()
info.print_flavors()

    