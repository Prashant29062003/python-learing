class Student:
    total_student = 0

    @staticmethod
    def greeting():
        return "Hello Bachooo!"

    def __init__(self,age = 0, name = "Unknown"):
        Student.total_student += 1
        self.__age = age
        self.__name = name
    
    # Eligant manner to intialize the getter and setter
    @property
    def age(self):
        # print("getter method called.")
        return self.__age

    @age.setter
    def age(self, a):
        if(a < 5):
            raise ValueError("You are not eligible for school! Go for play and keep learing and exploring! :)")
        # print("setter method called")
        self.__age = a
    
    # Alternative method
    def get__name(self):
        return self.__name

    def set__name(self, n):
        self.__name = n

    def get_details(self):
        return f"{self.__name}(age:{self.__age}): Welcome to guru-kul!"

    
new_student = Student()
new_student.age = 22
new_student.set__name("Prashant")
print(new_student.get_details())
print(Student.total_student)