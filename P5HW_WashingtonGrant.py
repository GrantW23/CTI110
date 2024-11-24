# Grant Washington
# 11/24/24
# P5HW
# Menu driven Program

import random

guess = ''
print('Welcome to Math Quiz')
print('')

num_guesses = 1
num_1 = random.randint(1, 101)
num_2 = random.randint(1, 101)


while True:
    print('Main Menu')
    print("--------------------")
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print('')
    selections = int(input('Please choose one of the menu options:'))
    if selections == 1:
        print(f' {num_1}')
        print(f'+{num_2}')
        add_correct_answer = num_1 + num_2
        guess = int(input('Enter Answer.'))
        while guess != add_correct_answer:
            if guess < add_correct_answer:
                print("Sorry guess is to Low.")
                guess = int(input("Try again: "))
                num_guesses += 1
            elif guess > add_correct_answer:
                print('Sorry guess is to high.')
                guess = int(input("Try again: "))
                num_guesses += 1
        print('Congratulations!!! Your answer is correct.')
        print(f'Number of guesses: {num_guesses}')
        print('')
    if selections == 2:
        print(f' {num_1}')
        print(f'-{num_2}')
        sub_correct_answer = num_1 - num_2
        guess = int(input('Enter Answer.'))
        while guess != sub_correct_answer:
            if guess < sub_correct_answer:
                print("Sorry guess is to Low.")
                guess = int(input("Try again: "))
                num_guesses += 1
            elif guess > sub_correct_answer:
                print('Sorry guess is to high.')
                guess = int(input("Try again: "))
                num_guesses += 1
        print('Congratulations!!! Your answer is correct.')
        print(f'Number of guesses: {num_guesses}')
        print('')
    if selections == 3:
        print('Thanks for playing...')
        print('Bye!!')
        break


