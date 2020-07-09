#help()

#import time
#time.sleep(5)

def search4vowels(phrase: str) -> set:
    """ Выводит гласные, найденные во введеном слове """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

    #return bool(found)
    #for vowel in found:
    #    print(vowel)
search4vowels('domy')
help(search4vowels)


def search4letters(phrase:str, letters:str='aeiou') -> set:
    """ Returns set of letters from phrase """
    return set(letters).intersection(set(phrase))
search4letters('galaxy', 'xyz')

def double(arg):
    print('Before: ', arg)
    arg=arg*2
    print('After: ', arg)

def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)