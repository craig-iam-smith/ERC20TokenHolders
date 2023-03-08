import csv
from collections import defaultdict

totals = defaultdict(float)

with open("tokenlist.json", "w") as text_file:
    text_file.write("[\n")
    with open('export-token.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            total = float(row['Balance'])
            total = total / 100000000
            print(row['HolderAddress'], total)
            text_file.write('     {\n')
            text_file.write('     "address": ' + "\"" + row['HolderAddress']+"\"" + ',\n')
            text_file.write('     "balance": ' + "\"" + str(total)+ "\"" + '\n')
            text_file.write('     },\n')
        text_file.write(']\n')


