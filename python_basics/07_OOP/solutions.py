class Car:
    total_car=0

    def __init__(self, brand, model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand + "!"

    def car_info(self):
        print(f"car name is {self.__brand}  {self.__model}")

    def fuel_type(self):
        return "Petrol or disel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def get_model(self):
        return self.__model

    


class ElectricCar(Car):
    
    def __init__(self,model, brand, battery_size):
        super().__init__(model,brand)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Connect charge"

electric_car=ElectricCar("tesla","model S", "85kWh")
print(isinstance(electric_car, Car))
print(isinstance(electric_car, ElectricCar))

# print(electric_car.battery_size)
# print(electric_car.brand)
# print(electric_car.get_brand())
# electric_car.car_info()
# print(electric_car.fuel_type())

safari=Car("Tata","Safari")
print(safari.fuel_type())

my_car=Car("toyota", "model1")
# print(my_car.brand)
print(my_car.get_model)

# print(my_car.car_info())

car_2=Car("Suziki","baleno")
# print(car_2.brand)
# print(car_2.model)

print(Car.total_car)
print(Car.general_description())


class Engine:
    def engine_info(self):
        return "This is engine"

class Battery:
    def battery_info(self):
        return "this is battery"

class ElectricTwo(Engine,Battery,Car):
    pass

Testla_S=ElectricTwo("tesla","S")
print(Testla_S.battery_info())
print(Testla_S.engine_info())