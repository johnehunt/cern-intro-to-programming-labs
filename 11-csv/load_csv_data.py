import csv

data = []
filename = 'temperatures.csv'

print('Loading file', filename)
try:
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_length = len(row)
            if row_length != 4:
                print('Error in data (length is not 4):', row)
                print('In line:', reader.line_num)
            else:
                data.append(row)
except Exception as exp:
    print(exp)

print('Finished reading file')
print(data)
