#Grant Washington
#09/29/24
#P1HW2
#create a program that does some basic math on numbers that are entered
# This program will take information asked subtract is from you budget. It will give you a remaining balance as well as a list of all the information you inputed



print("This program calculates and diplayes travel expenses")
budget= int(input("Enter budget:" ))
location=input("Enter your travel destination:" )
gas= int(input("How much  do you think youn will spend on gas?" ))
acc= int(input("Approximately, how much will you need for accomodation/hotel?" ))
food= int(input("Last, how much do you need for food?" ))
total=gas+acc+food
r_balance= budget-total
print('')
print("-------Travel Expenses-------")
print("Location:", location)
print("initial budget:", budget)
print('')
print("fuel:",gas)
print("accomodation:", acc)
print("Food:",food)
print('')
print("remaining Balance:",r_balance)




