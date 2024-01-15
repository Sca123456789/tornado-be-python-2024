class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number Served: {self.number_served}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

def change_number_served(restaurant, new_number):
    restaurant.set_number_served(new_number)

def main():
    restaurant1 = Restaurant("Sample Restaurant", "Italian")
    restaurant1.describe_restaurant()

    restaurant1.set_number_served(10)
    restaurant1.describe_restaurant()

    change_number_served(restaurant1, 20)
    restaurant1.describe_restaurant()

    restaurant2 = Restaurant("Another Restaurant", "Mexican")
    restaurant3 = Restaurant("Third Restaurant", "Japanese")

    restaurant2.describe_restaurant()
    restaurant2.set_number_served(15)
    restaurant2.describe_restaurant()

    restaurant3.describe_restaurant()
    restaurant3.set_number_served(25)
    restaurant3.describe_restaurant()

    restaurant1.increment_number_served(5)
    restaurant1.describe_restaurant()

if __name__ == "__main__":
    main()
