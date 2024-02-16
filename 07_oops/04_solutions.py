class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model


    def get_brand(self):
        return self.__brand


    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricClass(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


car_object = ElectricClass('tesla','model s', '80kwh')

print(car_object.full_name())
print(car_object.model)
print(car_object.battery_size)

# print(car_object.__brand)
print(car_object.get_brand())