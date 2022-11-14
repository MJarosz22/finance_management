import requests
import csv
import gspread
import time
import categoryLoader

# insert the month you want to update
MONTH = 'august'


class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 2)
        return amount


url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)

mbankFile = f"monthly-statements/{MONTH}/mbank-{MONTH}.csv"
abnFile = f"monthly-statements/{MONTH}/abn-{MONTH}.csv"

dictionary = categoryLoader.get_dictionary()
known = categoryLoader.get_known()


def mBankFin(file):
    transactions = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            date = row[0]
            name = row[1].strip()
            if "marcin jarosz" in name.lower() or "natych" in name.lower():
                continue
            amount = float(row[4].split(' ')[0].replace(',', '.'))
            currency = row[4].split(' ')[1]
            if currency != 'EUR':
                amount = converter.convert(currency, 'EUR', amount)
                currency == 'EUR'
            category = 'other'
            for known_name in known:
                if known_name in name.lower():
                    category = dictionary[known_name]
            transaction = (date, name, amount, currency, category)
            transactions.append(transaction)
        return transactions


def abnFin(file):
    transactions = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            currency = row[1]
            date = row[2][0:4] + '-' + row[2][4:6] + '-' + row[2][6:8]
            amount = float(row[6].replace(',', '.'))
            name = row[8]
            for x in range(9, len(row)):
                name += ' ' + row[x]
            if "marcin jarosz" in name.lower() or "natych" in name.lower():
                continue
            category = 'other'
            for known_name in known:
                if known_name in name.lower():
                    category = dictionary[known_name]
            transaction = (date, name, amount, currency, category)
            transactions.append(transaction)
    return transactions


sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rowsMbank = mBankFin(mbankFile)
rowsAbn = abnFin(abnFile)
abnFin(abnFile)
for row in rowsMbank:
    wks.insert_row([row[0], row[1], row[4], row[2]], 6)
    time.sleep(2)

for row in rowsAbn:
    wks.insert_row([row[0], row[1], row[4], row[2]], 6)
    time.sleep(2)
