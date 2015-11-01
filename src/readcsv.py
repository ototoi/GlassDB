import csv
with open('./tmp/OHARA20150327S_mod.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print row[1]



