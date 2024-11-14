import random

# Jazmine Legall
# 11/14/2024
# P5LAB
# Calculate dollars and cents into set categories: Building off of P3LAB, in assignmeent P5LAb will be adding module imports, loops and functions to complete the assignment: simulate a self check out


###################################################################################

# NOTES

# 1. total_owned ----> random ---> float
# 2. cash ----> get from user ---> float
# 3. cash_back ----> total_owned - cash ---> float


# Types of functions
# Calc Cashback
# disperse CashBack

###################################################################################

# Value returning funtcion
def calc_cash_back():
    # Generate a random float for amount owned to store
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")
    money = float(input("How much cash will you put in the self-checkout? "))
    # Calculate cash back
    money_back = money - total_owed
    return money_back





# Non-returning function
def disperse_cash_back(money):
    money = int(round(money * 100, 2)) # Converts integer into cents


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



# Create a main
def main():
    print('********************************************')
    print(f"{'************* Self Check Out ***************'}")
    print('********************************************')
    print()
    money_back = calc_cash_back()
    print()
    print(f"Change is: $ {money_back:.2f}") # Displays user input into money
    print()
    disperse_cash_back(money_back)
    print()
    print('********************************************')
    
# Call the main
if __name__ == '__main__':
    main()