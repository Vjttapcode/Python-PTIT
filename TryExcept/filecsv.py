import csv
a=[]
with open('addresses.csv') as file_csv:
    rows = csv.reader(file_csv)
    next(rows)
    for row in rows:
        a.append(row)
    a = sorted(a, key = lambda x : int(x[6]))
with open('res.csv', 'w', newline='') as my_addrsorted:
    writer = csv.writer(my_addrsorted)
    writer.writerow(['First name', 'last name', 'Street', 'City', 'State', 'Year'])
    writer.writerows(a)
