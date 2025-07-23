class Car:
    def __init__(self, brand, model):   # Constructor ==> __init__
        self.__brand = brand    # ==> __anything shows private name
        self.model = model
    
    '''Encapsulation'''
    # setter method
    def set_brand(self, brand):
        self.__brand = brand


    def get_details(self):
        return self.__brand + " !"

    '''polymorphism'''
    def fuel_type(self):
        return "Petrol or Deisel"
    
    def full_Display(self):
        return f"{self.__brand}: {self.model}"

''' Inhertence '''
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    '''polymorphism''' # ==> method overriding
    def fuel_type(self):
        return "Petrol or Deisel"


my_2nd_car = ElectricCar("Tesla", "Model S","battery")
my_2nd_car_desc = my_2nd_car.full_Display()
print(my_2nd_car_desc)
print("Fuel Type: ", my_2nd_car.fuel_type())

my_car = Car("Toyota", "Corola")
# print(my_car.__brand)
print(my_car.get_details())
my_car.set_brand("Prashant")
print(my_car.get_details())
print(my_car.model)
print("Fuel Type: ", my_car.fuel_type())

# my_new_car = Car("Tata","safari")
# print(my_new_car.model)
# print(my_2nd_car.get_details())

