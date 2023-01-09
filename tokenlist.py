import csv
from collections import defaultdict

totals = defaultdict(float)

with open('export-token.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        row['column_6'] = row['column_6'].replace(",","")
        if row['column_7'] in ('Transfer', '0x60806040'):
            totals[row['column_4']] -= float(row['column_6'])
            totals[row['column_5']] = totals.setdefault(row['column_5'], 0.0) + float(row['column_6'])

for x in totals:
    if x != '0x0000000000000000000000000000000000000000' and totals[x] != 0:
        print(x, totals[x])
