# Grant Washington
# 11/17/24
# P5Lab
# simulate a customer using a self-checkout machine

import random


def disperse_change(money_value):

    money_value = money_value * 100

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


owe = round(random.uniform(0.01, 100.00), 2)
print(f'You owe {owe}')
cash_given = float(input('How much cash will you put in the self-checkout? '))
change = cash_given - owe
print('')
disperse_change(change)
