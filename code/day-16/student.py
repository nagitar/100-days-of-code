import csv

with open('names.csv', 'r') as csv_files:
    csv_reader = csv.reader(csv_files)

    with open('new_names.csv', 'w') as new_files:
        csv.writer = csv.writer(new_files, delimiter='-')

     for line in csv_reader:
         print(line)
