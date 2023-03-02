def ageCalculator():
    name = input("What is your name? ")
    year = input("What year were you born? ")
    age = 2022 - int(year)
    print(name + ", you are " + str(age) + " years old.")
    if age % 2 == 0:
        print("Your age is even.")
        if age % 10 == 0:
            print("Your age is a perfect ten.")

ageCalculator()

# test