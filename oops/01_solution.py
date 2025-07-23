class Car:
    total_car = 0

    @staticmethod 
    def general_description():
        return "Cars are the 4th largest pollution producing factor!"


    def __init__(self, brand, model):   # Constructor ==> __init__
        Car.total_car += 1
        self.__brand = brand    # ==> __anything shows private name
        self.__model = model
    
    '''Encapsulation'''
    # setter method
    def set_brand(self, brand):
        self.__brand = brand


    def get_brand(self):
        return self.__brand + " !"

    '''polymorphism'''
    def fuel_type(self):
        return "Petrol or Deisel"
    
    def full_Display(self):
        return f"{self.__brand}: {self.__model}"

    '''Property decorator'''
    @property
    def model(self):
        return self.__model
    



''' Inhertence '''
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    '''polymorphism''' # ==> method overriding
    def fuel_type(self):
        return "Electricity"


my_2nd_car = ElectricCar("Tesla", "Model S","battery")
my_2nd_car_desc = my_2nd_car.full_Display()
print(my_2nd_car_desc)
print("Fuel Type: ", my_2nd_car.fuel_type())

print("-------------------")

my_car = Car("Toyota", "Corola")
# print(my_car.__brand)
# print(my_car.get_brand())
# my_car.set_brand("Prashant")
# print(my_car.get_brand())
print(my_car.full_Display())
print("Fuel Type: ", my_car.fuel_type())
print(my_car.model)

print("-------------------")
my_new_car = Car("Tata","safari")
print(my_new_car.model)
print(my_2nd_car.get_brand())

print("-------------------")
print(Car.total_car)

# # isinstance(obj, classinfo) ==> check the is object is an instance of that class which we compare (gives: true/false)
# if isinstance(my_2nd_car, Car):
#     print("Tesla Car is an instance of Car class")
# if isinstance(my_2nd_car, ElectricCar):
#     print("Tesla Car is an instance of Electric class")



''' Multiple Inheritance '''
class Battery:
    def battery_details(self):
        return "This is 4-octa multi-cellular battery."

class Engine:
    def engine_details(self):
        return "This is high performance and long lasting engine."
    

class ElectricCarTwo(Battery, Engine, Car):
    pass


new_electric_car = ElectricCarTwo("Tesla", "Model S")

print(new_electric_car.battery_details())
print(new_electric_car.engine_details())