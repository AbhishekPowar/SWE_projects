from random import randint
mode =  {1 : 20, 2 : 15, 3: 10}

print("Let's start\n I am choosing a number between 1 and 100")

comp_guess = randint(1,100)

print('Select mode : ')
print(f'1 - Easy\n2 - Medium\n3 - Hard')
tries_allowed = mode[int(input('Your choice of Mode : '))]

print('Start a guessing')
no_of_guess = 0
while no_of_guess < tries_allowed:
    no_of_guess += 1
    print(f'\nAttempt {no_of_guess} :')
    user_guess = int(input('Take a guess:'))
    if user_guess < comp_guess:
        print('Guess higher number')
    elif user_guess > comp_guess:
        print('Guess lower number')
    else:
        print(f'Congrtulations you got number right in {no_of_guess} attempts')
        break
    
else:
    print(f'You lose, you took {no_of_guess} attempts')


