# Jazmine Legall
# 09/30/2024
# P2HW1
# create a program that calculates and displays travel expenses
# Using P1HW2


# Input area
print('This program calculates and displays travel expenses')
print()
# Ask user to enter their budget
budget = float(input('Enter Budget: '))
print()
# Ask user to enter travel destination
travel = input('Enter your travel destination: ')
print()
# Ask user for amount they will spend on gas
gas = float(input('How much do you think you will spend on gas? '))
print()
# Ask user for amount they will spend on accommodation
accom = float(input('Approximately, how much will you need for accommodation/hotel? '))
print()
# Ask user for amount they will spend on food
food = float(input('Last, how much do you need for food? '))
# Add expenses
total = gas + accom + food
# Subtract expenses from budget
balance = budget - total

# Display results

# UPDATED: 9/30/2024 : added string formatiing to create columns
print()
print('------------Travel Expenses------------')
print(f"{'Location:':20} {travel:<20}")
print(f"{'Initial Budget:':20} ${budget:<19.2f}")
print(f"{'Fuel:':20} ${gas:<19.2f}")
print(f"{'Accommodation:':20} ${accom:<19.2f}")
print(f"{'Food:':20} ${food:<19.2f}")
print('---------------------------------------')
print()
print(f"{'Remaining Balance:':20} ${balance:<19.2f}")

# Extra just to view total var
# print('Added expenses:', total)
