def countCharactersCategory(phrase):
    total = {
        'specialCharacters': 0,
        'digits':0,
        'vowels':0,
        'consonants':0
    }
    answers = {
        'base': 'Total no. of',
        'options': [
            'vowels in the given string: ',
            'consonants in the given string: ',
            'digits in the given string: ',
            'of special characters in the given string: '
        ]
    }
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(0, len(phrase)):
        char = phrase[i]
        # Alphabets family
        if ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
            # Converting character to lower case
            char = char.lower()

            # Vowels
            if (char == vowels[0] or char == vowels[1] or char == vowels[2] or char == vowels[3] or char == vowels[4]):
                total['vowels'] += 1
            # Consonants
            else:
                total['consonants'] += 1

        # Digits family
        elif (char >= '0' and char <= '9'):
            total['digits'] += 1
        # Special characters family
        else:
            total['specialCharacters'] += 1

    print("Input string: ", phrase)
    print(answers['base'], answers['options'][0], total['vowels'])
    print(answers['base'], answers['options'][1], total['consonants'])
    print(answers['base'], answers['options'][2], total['digits'])
    print(answers['base'], answers['options'][3], total['specialCharacters'])

# Driver code
# Test case: 1
s1 = "Welcome 2 #MUO"
countCharactersCategory(s1)
# Test case: 2
s2 = "This Is @ InpuT String 2"
countCharactersCategory(s2)