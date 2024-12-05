# Jazmine Legall
# 09/17/2024
# P1LAB2
# Calculating Exponents using mathematical expression

print('----- Calculating Exponents -----')

# Get base value as int
baseValue = int (input('Enter an integer as the base value:  '))
exponent = int (input('Enter an integer as the exponent:  '))

total = baseValue ** exponent

print(baseValue, 'raised to the power of',exponent, 'is', total, '!!')

# Addition and Subraction
print('----- Addition and Subtraction -----')

startingInt = int(input('Enter a starting integer: '))
addInt = int(input('Enter an integer to add: '))
subInt = int(input('Enter an integer to subtract: '))

compTotal = startingInt + addInt - subInt;

print(startingInt, '+', addInt, '-', subInt, 'is equal to', compTotal )

