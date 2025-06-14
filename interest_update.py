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

# Processing of account
for account_number in customer_account:
    balance = customer_account[account_number]

    if balance >= 5000:
        interest = 0.05
    elif balance >= 1000:
        interest = 0.025
    elif balance > 0:
        interest = 0.01
    elif balance < 0:
        interest = 0.1
    else:
        interest = 0
 
        # Crediting interest in account balance
    customer_account[account_number] += balance * interest / 12
    pprint.pprint(customer_account) 


