# Grant Washington
# 11/3/24
# P4Lab2
# displays information to users using loops

repeat = ''
while repeat.lower() != 'no':
    num = int(input("Enter and integer:"))
    if num >= 0:
        for i in range(1, 13):
            product = num * i
            print(f'{num} * {i} = {product}')
    else:
        print("This program does not handle negative numbers")

    repeat = input('Would you like to the program to run again?')
print('Program Ended')
