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
with open("tokenlist.json", "w") as text_file:
    text_file.write("[\n")
    for x in totals:
        if x != '0x0000000000000000000000000000000000000000' and totals[x] != 0:
            text_file.write('     {\n')
            text_file.write('     "address": ' + x + ',\n')
            text_file.write('     "balance": ' + str(totals[x])+ '\n')
            text_file.write('     },\n')
    text_file.write(']\n')

with open("tokenlist.txt", "w") as text_file:
    for x in totals:
        if x != '0x0000000000000000000000000000000000000000' and totals[x] != 0:
            text_file.write(x + ',' + str(totals[x]) + "\n");

