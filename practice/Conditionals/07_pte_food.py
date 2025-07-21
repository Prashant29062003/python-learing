# Problem: Recommend a type of pet food based on the pet's species and age.(eg. Dog: <2 years - Puppy food, Cat:>5 years - Senior cat food)
pet_species = "dog"
pet_age = 1

if pet_species == "dog":
    if pet_age < 2:
        pet_food = "Puppy food"
    elif pet_age > 5:
        prt_food = "Senior dog food"
elif pet_species == "cat":
    if pet_age < 2:
        pet_food = "Cat food"
    elif pet_age > 5:
        prt_food = "Senior Cat food"

print(f"{pet_species.capitalize()} is need {pet_food}.")