import random
print("GUESS MY NUMBER started..")

print('Enter your  name :   ')
name    =   input()
print(f'Hello {name}, I am guessing a number between 1 and 100')

print("Ok let me think, I am done.")
secret_num=random.randint(1,100)

print('how many chances do you want :   ')
chances=int(input())

ans=[]
your_guess=list()
print('Now start guessing ')
for num_of_guess in range(1,chances+1):
    guess=int(input())
    your_guess.append(guess)
    low=0
    up=100
    if guess>secret_num:
        print('Too high')
        ans.append((low+guess)//2)
        low=guess
    elif guess<secret_num:
        print('Too low')
        ans.append((up+guess)//2)
        up=guess
    else:
        print(f'Yes {secret_num} ,You guessed my number in {num_of_guess} guesses')
        break
if num_of_guess >chances:
    print(f'Nope number i gussed was {secret_num} ')

#print(f'well played but u could do i just {len(ans)} tries')
#print (f'Best way was {ans}')
print(f'Your tried {your_guess}')