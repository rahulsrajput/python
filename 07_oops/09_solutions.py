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



car_object_1 = ElectricClass('tesla','model s', '80kwh')
print(isinstance(car_object_1,ElectricClass))
print(isinstance(car_object_1,Car))


car_object_3 = Car('Audi','X5')


