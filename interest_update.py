"""Interest update program"""

# Import statements
import pprint

# declaring a variable to store customers account date
customer_account = {}

# Printing data of account_balance files in the collection
with open("account_balances.txt", "r") as input_file:
    for line in input_file:
        account_number, balance = line.strip().split("|")
        customer_account[account_number] = float(balance)

pprint.pprint(customer_account)


