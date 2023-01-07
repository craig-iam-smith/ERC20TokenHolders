import csv
with open('export-token.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    totals = {'account': float(0.0)}
    for row in reader:
        row[6] = row[6].replace(",","")
        if (row[7] == 'Transfer') or (row[7] == '0x60806040'):
            if (row[4] in totals):
                totals[row[4]] = float(totals[row[4]]) - float(row[6])
            else:
                totals[row[4]] = float(row[6])
            if (row[5] in totals):
                totals[row[5]] = float(totals[row[5]]) + float(row[6])
            else:
                totals[row[5]] = float(row[6])
    for x in totals:
        if (x != '0x0000000000000000000000000000000000000000') and (totals[x] != 0):
            print (x, totals[x])