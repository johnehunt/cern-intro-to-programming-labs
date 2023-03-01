import csv

data = []
filename = 'accounts.csv'

print('Loading file', filename)
with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    print(f'header: {header}')
    for row in reader:
        row_length = len(row)
        if row_length != 2:
            print('Error in data (length is not 4):', row)
            print('In line:', reader.line_num)
        else:
            transaction = (row[0], row[1])
            data.append(transaction)

print('Finished reading file')
print(data)
