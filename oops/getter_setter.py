class Student:
    def __init__(self,age = 0, name = "Unknown"):
        self._age = age
        self._name = name
    
    # Eligant manner to intialize the getter and setter
    @property
    def age(self):
        # print("getter method called.")
        return self._age

    @age.setter
    def age(self, a):
        if(a < 5):
            raise ValueError("You are not eligible for school! Go for play and keep learing and exploring! :)")
        # print("setter method called")
        self._age = a
    
    # Alternative method
    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n

    def get_details(self):
        return f"{self._name}(age:{self._age}): Welcome to guru-kul!"

    
new_student = Student()
new_student.age = 22
new_student.set_name("Prashant")
print(new_student.get_details())