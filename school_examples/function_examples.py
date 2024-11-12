# About to create some user def functions


# Create a main function - all logic in code goes here


# We just defined a non value return function
def my_animal(name, sound, pound_food):
    print(f"The {name} makes {sound} noise!")
    print(f"The {name} eats {pound_food} pounds of food a day!")
    print(f"The {name} eats {pound_food * 7} pounds of food a week!")



def main ():
# when turning in assignments codes must be inside the main
    print(f"The main function is executing...")
    print()
# call animal function
    my_animal('cat', 'meow', 3)
    
# call the function
if __name__ == '__main__':
    main()