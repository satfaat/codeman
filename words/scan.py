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


def countOccurrences(str, ch):
    """
    program to count occurrences
    of a given character in a string
    Function to count the occurrences of
    the given character in the string
    """
    # Counter variable
    counter = 0
    for char in str:
        # check if the given character matches
        # with the character in the string
        if char == ch:
            # if the given character matches with
            # the character in the string,
            # increment the counter variable
            counter += 1
    return counter


# RUN TESTS
def test2():
    str1 = "she sells seashells by the seashore"
    ch1 = 's'
    print("Input string 1:", str1)
    print("Character", ch1, "has occured",
    countOccurrences(str1, ch1),"times in the given string.")
    str2 = "peter piper picked a peck of pickled peppers"
    ch2 = 'p'
    print("Input string 2:", str2)
    print("Character", ch2, "has occured",
    countOccurrences(str2, ch2),"times in the given string.")
    str3 = "I saw Susie sitting in a shoeshine shop"
    ch3 = 'a'
    print("Input string 3:", str3)
    print("Character", ch3, "has occured",
    countOccurrences(str3, ch3),"times in the given string.")
    str4 = "Near an ear, a nearer ear, a nearly eerie ear"
    ch4 = 'r'
    print("Input string 4:", str4)
    print("Character", ch4, "has occured",
    countOccurrences(str4, ch4),"times in the given string.")
    str5 = "He threw three free throws"
    ch5 = 'e'
    print("Input string 5:", str5)
    print("Character", ch5, "has occured",
    countOccurrences(str5, ch5),"times in the given string.")