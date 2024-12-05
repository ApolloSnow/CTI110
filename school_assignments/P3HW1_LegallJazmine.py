# Jazmine Legall
# 10/17/2024
# P3HW1
# Create a python file that calculates user grades and displays grades and average



    
# User inputs grades
# list 
mod_list = [
    float(input("Enter grade for Module 1: ")),
    float(input("Enter grade for Module 2: ")),
    float(input("Enter grade for Module 3: ")),
    float(input("Enter grade for Module 4: ")),
    float(input("Enter grade for Module 5: ")),
    float(input("Enter grade for Module 6: ")),
    ]

# math area for average
average = sum(mod_list) / len(mod_list)

print()
# Display area
print('-----------Results-----------')
print()
print(f"{'Lowest Grade:':20} {min(mod_list):<19.1f}")
print(f"{'Highest Grade:':20} {max(mod_list):<19.1f}")
print(f"{'Sum of Grades:':20} {sum(mod_list):<19.1f}")
print(f"{'Average:':20} {average:<19.2f}")
print()
print('-----------------------------')
if average >= 90:
    print('Your grade is: A')
elif average > 80:
     print('Your grade is: B')
elif average > 70:
     print('Your grade is: C')
elif average > 60:
     print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this
