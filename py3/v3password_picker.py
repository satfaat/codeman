import random
import string

adjectives = ['sleepy', 'slow', 'smelly',
              'wet', 'fat', 'red']
nouns = ['apple', 'dinosaur', 'ball']
print('Welcom to Password Picker!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s' % password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break
