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
choice = int(input('>'))

# checking balance
if choice == 1:
  print(f'You have ${customer_balance}')
  print('''
What would you like to do:
Press 2 for withdrawal
Press 3 to Transfer Funds
Press 4 to Exit
''')
  choice_1 = int(input('>'))
  if choice_1 == 4:
    print('Exiting...')
    sys.exit(0)
