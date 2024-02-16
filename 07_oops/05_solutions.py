class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model


    def get_brand(self):
        return self.__brand


    def fuel_type(self):
        return 'petrol or diesel'

    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricClass(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


    def fuel_type(self):
        return 'electric charge'



car_object_1 = ElectricClass('tesla','model s', '80kwh')
print(car_object_1.fuel_type())

car_object_2 = Car('BMW','XM')
print(car_object_2.fuel_type())