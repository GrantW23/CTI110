# Grant Washington
# 11/10/24
# P4HW2
# calculate gross pay, regular pay, and overtime pay for multiple employees

# collects all information gathered into lists
name = input('Enter employee''s name or "Done" to terminate: ')
employees = []
Total_rp = []
Total_OP = []
Total_GP = []

while True:
    worked_hours = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    employees.append(name)
# Finds out how much overtime the employee has
    if worked_hours > 40:
        OverTime = worked_hours - 40
        worked_hours -= OverTime
    else:
        OverTime = 0

# Calculates regular pay, overtime pay, and gross pay as well to the totals
    regular_pay = float(worked_hours * pay_rate)
    OverTime_pay = float(OverTime * pay_rate)
    gross_pay = float(regular_pay + OverTime_pay)
    Total_GP.append(gross_pay)
    Total_OP.append(OverTime_pay)
    Total_rp.append(regular_pay)
# displays information gather and processed from the employee entered
    print("------------------------")
    print(f'Employee name: {name}')
    print(f'Hours Worked     Pay rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
    print("------------------------------------------------------------------------------")
    print(f'{worked_hours: <16.1f} {pay_rate: <10.1f} {OverTime: <10.1f} {OverTime_pay: <14.2f} ${regular_pay: <13.2f} ${gross_pay: .2f}')
    name = input('Enter employee''s name or "Done" to terminate: ')
    if name.lower() == "done":
        break
# prints the information gathered of all the employees
print(f'Total number of employees entered: {len(employees)} ')
print(f'Total amount paid for overtime: ${sum(Total_OP)} ')
print(f'Total amount paid for regular hours: ${sum(Total_rp)} ')
print(f'Total amount paid for Gross: ${sum(Total_GP)} ')
