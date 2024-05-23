import csv

with open('DATA/baby-names.csv') as baby_names_in:
    rdr = csv.reader(baby_names_in)
    for record in rdr:
        if (record[1] == 'Sarah') and (record[3] == 'girl'):
            print(record)

