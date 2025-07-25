
def debug(func):
    def wrapper(*args, **kwargs):
        arg_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}: {v}\t" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args {arg_value} and kwargs {kwargs_value}.")
        return func(*args, **kwargs)
    return wrapper



@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Prashant", greeting="Hanji")


@debug
def hello():
    print("Hello")