# Funciton with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.abs

# def print_kwargs(name, power):
#     print("Name: ", name, "power: ", power)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Prashant", power="run", enemy="no one")