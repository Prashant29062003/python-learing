class Vehicle:

    vehicle_count = 0

    def __init__(self, brand="Unknown", wheels=0):
        Vehicle.vehicle_count += 1
        self.__brand = brand
        self.__wheels = wheels
    
    @property
    def brand(self):
        return self.__brand
    
    @staticmethod
    def general_info():
        return "Vehicles are used for transport."

    def fuel_type(self):
        return "Generic Fuel"

    def show_details(self):
        print(f"Brand: {self.__brand}, Wheels: {self.__wheels}")

# Mixin class
class SmartFeatures:
    def auto_parking(self):
        return "Auto Parking Activated!"
    
    def voice_assist(self):
        return "Voice Assistant Ready."

class SmartCar(SmartFeatures, Vehicle):
    def __init__(self, brand, wheels = 4):
        super().__init__(brand, wheels)
    
    def fuel_type(self):
        return "Electric"

    def activate_safety_mode(self):
        if(self.brand == "Unknown"):
            raise UnknownBrandError("Brand not recognized. Cannot activate safety mode!")
        else:
            return "Safety Mode Activated"

class UnknownBrandError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Bike(Vehicle):
    def __init__(self,brand, wheels = 2):
        super().__init__(brand, wheels)

    def fuel_type(self):
        return "Petrol"

class Truck(Vehicle):

    def __init__(self, brand, wheels = 6):
        super().__init__(brand, wheels)

    def fuel_type(self):
        return "Diesel"


# bike_1 = Bike("Honda")
# bike_1.show_details()
# print(bike_1.fuel_type())

# truck_1 = Truck("Tata")
# truck_1.show_details()
# print(truck_1.fuel_type())

# truck_2 = Truck("Mahindra")
# truck_2.show_details()
# print(truck_2.fuel_type())

# print(Vehicle.vehicle_count)

Tesla = SmartCar("Tesla")
print(Tesla.fuel_type())
print(Tesla.activate_safety_mode())

another_car = SmartCar("Unknown")
try:
    print(another_car.activate_safety_mode())
except UnknownBrandError as e:
    print("Enter Brand name!")


print(Vehicle.vehicle_count)