# Grant Washington
# 10/20/24
# P3HW2_Salary
# Gathers information about working employees and displays the info in a nice display

# Gathers this information needed for the program to work

name = input("Enter employee's name: ")
worked_hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


# Finds out how much overtime the employee has
if worked_hours > 40:
    OverTime = worked_hours - 40
else:
    OverTime = 0

# Calculates regular pay, overtime pay, and gross pay
regular_pay = float(worked_hours * pay_rate)
OverTime_pay = float(OverTime * pay_rate)
gross_pay = float(regular_pay + OverTime_pay)

# displays information gather and processed
print("------------------------")
print(f'Employee name: {name}')
print(f'Hours Worked     Pay rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
print("------------------------------------------------------------------------------")
print(f'{worked_hours: <16.1f} {pay_rate: <10.1f} {OverTime: <10.1f} {OverTime_pay: <14.2f} ${regular_pay: <13.2f} ${gross_pay:.2f}')
