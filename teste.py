import csv
 
data = csv.reader(open('teste.csv', 'r'))
for rows in data:
    print (rows)
   