# Jazmine Legall
# 10/23/2024
# P3LAB
# Calculate dollars and cents into set categories 


# Get user money value
money = float(input('Enter the amount of money as a float: $'))
money = int(round(money * 100)) # Converts integer into cents


# Area for vars for dollars/cents
# Calculate number of dollars
dollars = money // 100
money = money % 100

# Calculate the remaining cents, starting with quarters down to pennies
# Quarters
quarters = money // 25
money = money % 25
# Dimes
dimes = money // 10
money = money % 10
# Nickels
nickels = money // 5
money = money % 5
# Pennies
pennies = money


# Branches
# Output Area
if dollars > 0 :
    print(f"{dollars} Dollar"
    if dollars == 1 else
    f"{dollars} Dollars")
if quarters > 0 :
    print(f"{quarters} Quarter"
    if quarters == 1 else
    f"{quarters} Quarters")
if dimes > 0 :
    print(f"{dimes} Dime"
    if dimes == 1 else
    f"{dimes} Dimes")
if nickels > 0 :
    print(f"{nickels} Nickel"
    if nickels == 1 else
    f"{nickels} Nickels")
if pennies > 0 :
    print(f"{pennies} Penny"
    if pennies == 1 else
    f"{pennies} Pennies")

# When input is Zero
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print('No change')