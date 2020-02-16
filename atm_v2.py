import sys

customer_balance = 500000
customer_pin = '1982'

def verify_pin(pin):
  if pin != customer_pin:
    return False
  return True

def login():
  tries = 1
  while tries < 5:
    print('Enter your 4 digit pin')
    pin = input('> ')
    if not verify_pin(pin):
      print('invalid pin')
      tries += 1
    else:
      print('pin accepted')
      return True

def welcome_screen():
  if not login():
    print('exiting...')
    sys.exit(1)
  print('''
Welcome to the Bank of Moolah
To continue, Use the following instruction
Press 1 to check balance
Press 2 for withdrawal
Press 3 to Transfer Funds
Press 4 to Exit
''')
  while True:
    choice = int(input('Enter the operation: '))
    if choice == 1:
      check_balance()
    if choice == 2:
      amount = 0
      withdrawal(amount)
    elif choice == 3:
      account_number = input('enter account number: ')
      amount = int(input('Enter an amount: '))
      transfer(amount,account_number)
    elif choice == 4:
      break
  sys.exit(0)

def check_balance():
  print(f'You have ${customer_balance}')
  return

def withdrawal(amount):
  global customer_balance
  print('How much do you want to withdraw')
  amount = int(input('> '))
  if customer_balance > amount:
    print(f'Withdrawing {amount}...')
    customer_balance = customer_balance - amount
    print(customer_balance)
    return
  else:
    print('''Sorry you do not have that amount.
    Try Checking your balance
    Exiting...''')
    return

def transfer(amount,account_number):
  global customer_balance
  if customer_balance >= amount:
    print(f'Transfering {amount} to {account_number}...')
    customer_balance = customer_balance - amount
    print(customer_balance)
  else:
    print('''Sorry you do not have that amount.
  Try Checking your balance
  Exiting...''')

def main():
  welcome_screen()

if __name__ == "__main__":
  main()