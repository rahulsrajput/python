class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        # self.total_car += 1
        Car.total_car += 1


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


class Battery():
    def battery_info(self):
        return 'this is battery'

class Engine():
    def engine_info(self):
        return 'this is engine'

class ElectricCar2(Battery, Engine, Car):
    pass



car_object_1 = ElectricClass('tesla','model s', '80kwh')


new_car_object = ElectricCar2('Audi','EV')
print(new_car_object.engine_info())
print(new_car_object.battery_info())
print(isinstance(new_car_object,ElectricCar2))
print(isinstance(new_car_object,Car))
print(isinstance(new_car_object,Battery))
print(isinstance(new_car_object,Engine))
print(isinstance(new_car_object,ElectricClass))

