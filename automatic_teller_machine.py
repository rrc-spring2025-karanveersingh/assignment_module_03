"""Automatch Teller machine Simulator Program"""

__author__ = "Karanveer Singh Gill"
__version__ = "1.0.0"

# Importing Files
import random 
import time
import os
# Defining menu

menu_option = {"D","W","Q"}

# Generating initial balance
initial_balance = random.randint(-1000,10000)

# Display Selection Menu
while True:
   print("*" * 40)
   print("PIXELL RIVER FINANCIAL".center(40))
   print("ATM Simulator" .center(48))
   print()
   print(f"Your current balance is: ${initial_balance:,.2f}")
   print("Deposit: D" .center(40))
   print("Withdraw: W".center(40))
   print("Quit:Q".center(40))
   print("*" * 40)

    # Menu Selection Prompt

   selection = input("Enter your selection: ").upper().strip()
   # Menu selection validation
   if selection not in menu_option:
    print()
    print("*" * 48)
    print("Invalid selection".center(40))
    print("*" * 40)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    continue
   # Documentation related to condition
   if selection == "Q":
    break 
   # Deposit/ Withdraw
   amount = float(input("Enter the transaction amount"))
   if selection == "D":
       initial_balance += amount
       print("*" * 40)
       print(f"Your current balance is: ${initial_balance:,.2f}")
       print("*" * 40)

    # Withdraw
   if selection == "W":
        if amount > initial_balance:
            print()
            print("*" * 40)
            print("INSUFFICIENT FUNDS".center(40))
            print("*" * 40)
            print()
            print("*" * 40)
            print(F"Your current balance is: ${initial_balance:,.2f}")
            print("*" * 40)
            
        else:
            initial_balance -= amount
            print()
            print("*" * 40)
            print(F"your current balance is: ${initial_balance:,.2f}")
            print("*" * 40)
        time.sleep(3)
