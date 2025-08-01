import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_function(a,b):
    time.sleep(4)
    # some heavy work like database calling or hopping whcih increases latency
    return a + b

print(long_running_function(2, 3))
print(long_running_function(3,1))