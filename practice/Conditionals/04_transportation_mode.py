dist = int(input("Enter your distance from in km: "))
mode = "Walk"
if dist < 3:
    mode = "Walk"
elif dist <= 15:
    mode = "Bike"
else:
    mode = "Car"

print(f"Mode of transportation is by {mode} for {dist}km.")