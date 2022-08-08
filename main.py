import csv
import gspread
import time

MONTH = 'july'

file = f"mbank-pln-{MONTH}.csv"


def mBankFin(file):
    transactions = []
    sum = 0
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        for row in csv_reader:
            date = row[0] #date
            name = row[1].strip() #description
            #print(row[2]) #account
            #print(row[3]) #category
            amount = float(row[4].split(' ')[0].replace(',', '.')) #amount
            sum += amount
            currency = row[4].split(' ')[1]
            category = 'other'
            transaction = (date, name, amount, currency, category)
            transactions.append(transaction)
        return transactions

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = mBankFin(file)

for row in rows:
    wks.insert_row([row[0], row[1], row[3], row[2]], 8)
    time.sleep(2)