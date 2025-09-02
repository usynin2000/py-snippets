import csv

# easiest way to work with csv files

with open("data/test_file.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(type(row))