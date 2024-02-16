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
    

    @staticmethod
    def car_desc():
        return 'Car are means of transportation'


class ElectricClass(Car):
  

    def __init__(self,brand, model, battery_size):
        
        super().__init__(brand,model)
        self.battery_size = battery_size



    def fuel_type(self):
        return 'electric charge'



# car_object_1 = ElectricClass('tesla','model s', '80kwh')
# print(car_object_1.fuel_type())




# car_object_2 = Car('BMW','XM')
# print(car_object_2.fuel_type())

car_object_3 = Car('Audi','X5')


print(car_object_3.car_desc())
print(Car.car_desc())