# Jazmine Legall
# 09/26/2024
# P2LAB2
# Creating a program that creates a dicitionary with key
# and value pairs

# The keys represent an automobile
# The value represents the MPG for that vehicle



# creating an array for keys and values
keyAuto = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26,
    }

# Creates a variable that holds all the keys in the dictionary
keys = keyAuto.keys()
print(keys)
print()
vehicle = input("Enter a vehicle to see it's mpg: ")

# if statement that matches input to vehicle and outputs vehicle and mpg
if vehicle in keyAuto:
    mpg = keyAuto[vehicle]
    print()
    print(f"The {vehicle} gets {mpg} mpg.")
    
    print()
# user input how much they plan to drive
drive = float(input(f"How many miles will you drive the {vehicle}? "))
#calculates the gallons of gas needed
gallons_needed = drive / mpg

print()
# Displays gallons needed, rounded to two decimal places
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {drive} miles.")
