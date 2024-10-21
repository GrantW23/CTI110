# Grant Washington
# 10/20/24
# P3Lab
# Allows the user to enter money and receive the efficient number of dollars, and coins needed

money_value = input("Enter the amount of money as a float: ")
if money_value[0] == "$":
    money_value = float(money_value[1:])
else: money_value = float(money_value)

money_value = money_value * 100

if money_value == 0:
    print("No change")

dollars = int(money_value // 100)
money_value %= 100

quarters = int(money_value // 25)
money_value %= 25

dimes = int(money_value // 10)
money_value %= 10

nickles = int(money_value // 5)
money_value %= 5

pennies = int(money_value)

if dollars == 1:
    print(f'{dollars} Dollar')
elif dollars == 0:
    pass
else:
    print(f'{dollars} Dollars')

if quarters == 1:
    print(f'{quarters} Quarter')
elif quarters == 0:
    pass
else:
    print(f'{quarters} Quarters')

if dimes == 1:
    print(f'{dimes} Dime')
elif dimes == 0:
    pass
else:
    print(f'{dimes} Dimes')

if nickles == 1:
    print(f'{nickles} Nickle')
elif nickles == 0:
    pass

else:
    print(f'{nickles} Nickles')
if pennies == 1:
    print(f'{pennies} Penny')
elif pennies == 0:
    pass
else:
    print(f'{pennies} Pennies')





