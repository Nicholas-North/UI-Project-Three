import csv

def getParts():
    parts = []
    with open('Parts.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            parts.append(row)
    return parts