coffeeSize = input("Enter your coffee size (Small / Medium / Large): ").lower()
coffeeOption = input("Want extra short of esperroso(y/n): ").lower()


if coffeeOption == 'y':
    coffee = coffeeSize.capitalize() + " coffee with an extra short of esperesso!"
else:
    coffee = coffeeSize.capitalize() + " coffee."

print("Order: ", coffee)
