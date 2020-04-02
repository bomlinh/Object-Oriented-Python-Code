# Non-OOP Bank
# Version 4
# Any number of accounts - with lists

accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)
   
def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Account', accountNumber)
    print('       Name', accountNamesList[accountNumber])
    print('       Balance:', accountBalancesList[accountNumber])
    print('       Password:', accountPasswordsList[accountNumber])
    print()

def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return -1
    return accountBalancesList[accountNumber]

def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return -1
        
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return -1
    
    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] + amountToDeposit
    return accountBalancesList[accountNumber]
    
def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return -1

    if amountToWithdraw > accountBalancesList[accountNumber]:
        print('You cannot withdraw more than you have in your account')
        return -1

    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password for this account')
        return -1
    
    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] - amountToWithdraw
    return accountBalancesList[accountNumber]

# Create two sample accounts
print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100.00, 'soup')

print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345.67, 'nuts')

while True:
    print()
    print('Type b to get the balance')
    print('Type d to make a deposit')
    print('Type n to create a new account')
    print('Type w to make a withdrawal')
    print('Type s to show all accounts')
    print('Type q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower() # force lower case
    action = action[0]  # just use first letter
    print()
    
    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance >= 0:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber= input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = float(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance >= 0:
            print('Your new balance is:', newBalance)
        
    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = input('How much money to have to start your account with? ')
        userStartingAmount = float(userStartingAmount)
        userPassword = input('What password would you like to use for this account? ')

        userAccountNumber = len(accountNamesList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    elif action == 's':   #show all
        print('Show:')
        nAccounts = len(accountNamesList)
        for accountNumber in range(0, nAccounts):
            show(accountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = float(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
 
        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance >= 0:
            print('Your new balance is:', newBalance)       

print('Done')