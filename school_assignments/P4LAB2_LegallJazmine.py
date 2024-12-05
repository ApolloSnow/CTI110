# Jazmine Legall
# 10/30/2024
# P4LAB2
# Create a program that asks the user to enter an integer and displays multiplication of user integer from 1 to 12


# User input integer

user_int = int(input('Enter an integer: '))
print()


# Starting While loop
while True:
# Initialize a if statement
    if user_int >= 0:
# Stating range 1 to 12 ( 13 so it stops at 12)
            for i in range(1, 13):
# Display users integer and multiplcation to 12
                print(f"{user_int} x {i} = {user_int * i}")
    else:
        print('\nCannot accept negative values...')

            
# Does the user want to run again
    run_again = input('\nWould you like to run the program again? (yes/no): ')
# If yes
    if run_again == 'yes':
# Ask user for new integer
        user_int = int(input('\nEnter an integer: '))
        print()
# If user does not want to run again
    else:
        print('\nGoodbye!')
        break
