import math
import decimal
def circle_stats(r):
    d = decimal.Decimal
    area = d(math.pi * r ** 2).quantize(d("0.01"))
    circum = d(2 * math.pi * r).quantize(d("0.01"))

    return {"area": area, "circumference": circum}

circle1 = circle_stats(3)
for i in circle1.keys():
    print(i, ": ", circle1[i])
