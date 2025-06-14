"""Interest update program"""
__author__ = "Karanveer Singh Gill"
__version__ = "1.0.0"
# Import statements
import pprint
import csv

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

# Storing the updated data

new_file = "updated_balances_KG.csv"

# Adding data in csv file
with open(new_file, "w") as output_file:
    output_file.write("Account,Balance\n")

# using loop in csv file for adding data
    for account_number, balance in customer_account.items():
        output_file.write(f"{account_number},{balance}\n")

    print(f"The file {new_file} created sucessfully|")

# Printing the data by use of DictReader function
with open("updated_balances_KG.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Account: {row["Account"]}, Balance: {row["Balance"]}")
              


