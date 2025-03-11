def show_balance(balance):
    print(f"Your balance is {balance}")
def deposit():
    deposit_amount = int(input('Enter the amount you want to deposit :'))
    return deposit_amount
def withdraw():
    withdraw_amount = int(input('Enter the value to withdraw :'))
    return withdraw_amount

def main():
    balance = 0
    is_running = True
    while is_running:
      
      print('Welcome to the banking program')
      print('------------------------------')
      print('1.Check balance'
      '\n 2.Deposit'
      '\n 3.Withdraw'
      '\n 4.Exit')
      choice = str(input('Enter your choice :'))
      if choice == '1':
          show_balance(balance)
      elif choice == '2':
          balance = balance + deposit()
      elif choice == '3':
          balance -= withdraw()
      elif choice == '4':
          is_running = False
      else:
          print('Invalid choice')

main()
