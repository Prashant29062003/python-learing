# Polimorphism in funciton
# WAF multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(p1,p2):
    return p1 * p2

print(multiply(2,3))
print(multiply(2,'p'))
print(multiply('t',10))