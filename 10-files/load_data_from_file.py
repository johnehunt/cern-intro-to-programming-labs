from datetime import datetime

print('Opening file')

with open('date_file.txt', 'r') as file:
    print('Reading contents)')
    lines = file.readlines()
    print('Accessing first line')
    date_str = lines[0]
    print('Date as a string:', date_str)
    datetime_object = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    print('Date as an object:', datetime_object)


print('Done')
