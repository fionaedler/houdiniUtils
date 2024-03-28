import csv

with open("data_sets/sentimentdataset.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)