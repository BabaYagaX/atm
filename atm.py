import sys

customer_balance = 500000
customer_pin = '1982'

# login user
tries = 1
while tries < 5:
  print('Enter your 4 digit pin')
  pin = input('> ')
  if pin == customer_pin:
    print('access granted')
    break 
  else:
    print('Invalid pin')
    tries += 1
  print('Too many incorrect tries.Try again in 20 minutes')
  print('Exiting...')

# welcome screen
print('''
Welcome to the Bank of Moolah
To continue, Use the following instruction
Press 1 to check balance
Press 2 for withdrawal
Press 3 to Transfer Funds
Press 4 to Exit
''')
choice = int(input('> '))

# checking balance
if choice == 1:
  print(f'You have ${customer_balance}')
  print('''
What would you like to do:
Press 2 for withdrawal
Press 3 to Transfer Funds
Press 4 to Exit
''')
  choice_1 = int(input('> '))
  if choice_1 == 4:
    print('Exiting...')
    sys.exit(0)

# withdrawal
if choice == 2:
  print('How much do you want to withdraw')
  amount = int(input('> '))
  if customer_balance > amount:
    print(f'Withdrawing {amount}...')
    customer_balance = customer_balance - amount
    print(customer_balance)
  else:
    print('''Sorry you do not have that amount.
    Try Checking your balance
    Exiting...''')
    sys.exit(1)

# transfer funds
if choice == 3:
  account_number = input('Enter account number: ') 
  amount = int(input('Enter amount you need to transfer:'))
  if customer_balance >= amount:
    print(f'Transfering {amount} to {account_number}...')
    customer_balance = customer_balance - amount
    print(customer_balance)
  else:
    print('''Sorry you do not have that amount.
  Try Checking your balance
  Exiting...''')
  sys.exit(1)

# exit
if choice == 4:
  print('Exiting...')
  sys.exit(0)