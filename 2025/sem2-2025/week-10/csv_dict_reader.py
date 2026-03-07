import csv
with open('data.csv', 'r') as fp:
    my_reader = csv.DictReader(fp)
    print(list(my_reader))

    