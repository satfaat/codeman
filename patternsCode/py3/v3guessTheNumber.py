# Game
import random

secretNumber = random.randint(1, 20)
print('try to guess the number from 1 to 20')

for guessesTaken in range (1, 7):
    print ('your guess')
    guess = int(input())

    if guess < secretNumber:
        print('it is less than guess number')
    elif guess > secretNumber:
        print('It is more then guess number')
    else:
        break # the right answer
    
if guess == secretNumber:
    print('you are right, guess trys: ' + str(guessesTaken))
else:
    print('No. the number is: ' + str(secretNumber))
    
