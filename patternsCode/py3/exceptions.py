try:
    a = float(input('Enter a number: '))
except ValueError:
    print("You entered an invalid number")

try:
    a = Fraction(input('Enter a fraction: '))
except ZeroDivisionError:
    print('Invalid fraction')
