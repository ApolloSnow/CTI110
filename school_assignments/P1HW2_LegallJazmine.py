# Jazmine Legall
# 09/22/2024
# P1HW2
# create a program that calculates and displays travel expenses


# Input area
print('This program calculates and displays travel expenses')
print()
# Ask user to enter their budget
budget = int(input('Enter Budget: '))
# Ask user to enter travel destination
travel = input('Enter your travel destination: ')
# Ask user for amount they will spend on gas
gas = int(input('How much do you think you will spend on gas? '))
# Ask user for amount they will spend on accommodation
accom = int(input('Approximately, how much will you need for accommodation/hotel? '))
# Ask user for amount they will spend on food
food = int(input('Last, how much do you need for food? '))
# Add expenses
total = gas + accom + food
# Subtract expenses from budget
balance = budget - total

# Display results
print()
print('------------Travel Expenses------------')
print('Location:', travel)
print('Initial Budget:', budget)
print()
print('Fuel:', gas)
print('Accommodation:', accom)
print('Food:', food)
print()
print('Remaining Balance:', balance)

# Extra just to view total var
# print('Added expenses:', total)