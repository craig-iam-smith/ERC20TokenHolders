import csv
from collections import defaultdict

totals = defaultdict(float)

with open('export-token.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        row['Quantity'] = row['Quantity'].replace(",","")
        if row['Method'] in ('Transfer', '0x60806040'):
            totals[row['From']] -= float(row['Quantity'])
            totals[row['To']] = totals.setdefault(row['To'], 0.0) + float(row['Quantity'])

for x in totals:
    if x != '0x0000000000000000000000000000000000000000' and totals[x] != 0:
        print(x, totals[x])
