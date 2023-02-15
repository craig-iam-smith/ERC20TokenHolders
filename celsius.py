import csv
from datetime import datetime
from collections import defaultdict
date_format = '%B %d, %Y %I:%M %p'
totals = defaultdict(float)
total = 0.0

with open('celsius.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader: 
        
        date = datetime.strptime(row[' Date and time'], date_format)
        if date.year >= 2022: 
        
            if row[' Transaction type'] == 'Reward':
                total += float(row[' USD Value'])
                              
                print (row[' USD Value'])
formatted = "${:,.2f}".format(total)
print (formatted)
   
