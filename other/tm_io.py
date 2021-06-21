# Output
    print('some text')

# input
    myName = input()
    person = input('What is your name? ')

# Example v3:
print('Hello')
print('What is your name? ') # запрос имени
myName = input()

print("It's good to meet you, " + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age? ') # Запрос возраста
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year.')
# end

# short version
    print('Hello, World')
    person = input('What is your name? ')
    print('Hello, ', person)
# end

tasks = open('todos.txt')
for chore in tasks:
    print(chore, end='')
tasks.close()

with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')