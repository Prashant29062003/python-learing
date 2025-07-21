# Fruit Conditions

fruit = "Banana"
print(f"Available {fruit}.")
fruitColor = int(input("Enter fruit color (green / yellow / brown): in form of 1/2/3: "))

if fruit == "Banana":
    if fruitColor == 1:
        condition = "Unripe"
    elif fruitColor == 2:
        condition = "Ripe"
    elif fruitColor == 3:
        condition = "Overripe"
    else:
        condition = "Unknown Color"

print(f"{fruit} is {fruitColor} then this is {condition}.")