# Non-OOP
# Bank 2
# Single account

accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

def menu():
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

def newAccount(name, balance, password):
    """
    to create accounts with 3 fields
    """
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)

def show(accountNumber):
    """
    display account informatiom by account number
    """
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNumber = int(accountNumber)
    print('Account', accountNumber)
    print(' Name', accountNamesList[accountNumber])
    print(' Balance:', accountBalancesList[accountNumber])
    print(' Password:', accountPasswordsList[accountNumber])
    print()

def getBalance(accountNumber, password):
    """
    return value of balance for account number
    """
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != accountPassword:
        print('Incorrect password')
        return None

    accountBalance += amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPassword:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None
    accountBalance -= amountToWithdraw
    return accountBalance

# create an account
print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')
print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345, 'nuts')

while True:
    menu()

    action = input('What do you want to do? ')
    action = action.lower() # force lowercase
    action = action[0] # just use first letter
    print()

    if action == 'q':
        break
    elif action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 's': # show
            print('Show:')
            userAccountNumber = input('Please enter your account number: ')
            show(userAccountNumber)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
print('Done')