# function with *args 
# WAF that takes variable number of arguments and returns thier sum

def sum_all(*args):
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5,6))
    