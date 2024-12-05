# Jazmine Legall
# 10/24/2024
# P3HW2
# Collecting User/Employee name, hours worked, and pay rate


# User/Employee input
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Pay variables
reg_hours = 40 # Standard full-time hours
overtime_hours = 0.0
overtime_pay = 0.0

# Checking if employee worked overtime
if hours > reg_hours :
    overtime_hours = hours - reg_hours
    overtime_pay = overtime_hours * pay_rate * 1.5
    reg_pay = reg_hours * pay_rate
else :
    # No overtime, calculates regular pay
    reg_pay = hours * pay_rate


# Calculate total gross pay
gross_pay = reg_pay + overtime_pay


# Display employee pay details
print('--------------------------------------')
print(f"{'Employee name:':15} {name}")
print()
print(f"{'Hours Worked':15} {'Pay Rate':15} {'OverTime':15} {'OverTime Pay':18} {'Regular Pay':15} {'Gross Pay'}")
print('--------------------------------------------------------------------------------------------------------------------')

# Display the pay breakdown
print(f"{hours:<15.1f} {pay_rate:<15.1f} {overtime_hours:<15.1f} {overtime_pay:<18.2f} ${reg_pay:<15.2f} ${gross_pay:.2f}")      
