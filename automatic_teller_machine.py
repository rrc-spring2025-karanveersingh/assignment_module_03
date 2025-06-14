"""Automatch Teller machine Simulator Program"""

__author__ = "Karanveer Singh Gill"
__version__ = "1.0.0"

# Importing Files
import random

# Defining menu

menu_option = {"D","W","Q"}

# Generating initial balance
initial_balance = random.randint(-1000,10000)

# Display Selection Menu
print("*" * 40)
print("PIXELL RIVER FINANCIAL".center(40))
print("ATM Simulator" .center(48))
print()
print(f"Your current balance is: ${initial_balance:,.2f}")
print("Deposit: D" .center(40))
print("Withdraw: W".center(40))
print("Quit:Q".center(40))
print("*" * 40)
