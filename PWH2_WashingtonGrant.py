# Grant Washington
# 10/13/24
# P1HW2
# create a program that does some basic math on numbers that are entered

# Tells the user what the program will do
print("This program calculates and displays travel expenses")

# the following inputs function take in info about how much the user is spending
budget = float(input("Enter budget:"))
location = input("Enter your travel destination:")
gas = float(input("How much  do you think you will spend on gas?"))
acc = float(input("Approximately, how much will you need for accommodations/hotel?"))
food = float(input("Last, how much do you need for food?"))

# This calculates the total and the remaining balance the user has
total = gas+acc+food
r_balance = budget-total

# These print statements shows the users budget, how much they spend, and the remaining balance
print('')
print("-------Travel Expenses-------")
print(f'Location:          {location:}')
print(f'initial budget:   ${budget:.2f}')
print(f'fuel:             ${gas:.2f}')
print(f'accommodation:    ${acc:.2f}')
print(f'Food:             ${food:.2f}')
print("-----------------------------")
print(f'Remaining Balance ${r_balance:.2f}')
