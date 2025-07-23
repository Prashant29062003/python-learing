# Generator Function with yields
# Problem: Write a generator funciton that yields even numbers up to specified limit. 

def sum_of_Nums(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

sum_of_Nums(fName="Prashant", lName="Kumar")