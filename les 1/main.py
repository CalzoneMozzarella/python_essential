class Auto:
    list_of_objects = []

    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

        Auto.list_of_objects.append(self)

    def set_dict(self):
        return {'name': self.name, 'model': self.model, 'price': self.price}


car1 = Auto('BMW', 'x5', 123)
car2 = Auto('BMW', 'x5', 123)
car3 = Auto('BMW', 'x5', 123)
car4 = Auto('BMW', 'x5', 123)
car5 = Auto('BMW', 'x5', 123)

list_for_printing = []

for car in Auto.list_of_objects:
    list_for_printing.append(car.set_dict())

print(list_for_printing)
