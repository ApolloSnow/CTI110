# About to create some user def functions


# Create a main function - all logic in code goes here


# We just defined a non value return function
def my_animal(name, sound, pound_food):
    print(f"The {name} makes {sound} noise!")
    print(f"The {name} eats {pound_food} pounds of food a day!")
    print(f"The {name} eats {(pound_food * 7) } pounds of food a week!")

 

# creating new function withh return
def getName():
    name = input("Enter your name: ")
    return name + " " + '*******'

def displayName(first):
    lastName = input("Enter your Last name: ")
    fullName = first + " " + lastName
    return fullName + " " + '*******'



# main area
def main ():
# when turning in assignments codes must be inside the main
    print(f"The main function is executing...")
    print()
# Call the value returning funtcion
    myName = getName()
    print(myName)
    print()
# call animal function
    my_animal('cat', 'meow', 3)
    print()
    my_animal('Lion', 'rawr',  10)
    print()
# Call name
    print(displayName(myName))




# call the function
if __name__ == '__main__':
    main()