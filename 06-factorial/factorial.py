print('Starting factorial calculation program')
input_number = input('Please input the number: ')
print(f'The number to calculate factorial for is {input_number}')

if input_number.startswith('-'):
    print('Factorial not defined for negative numbers')
elif input_number.isnumeric():
    num = int(input_number)

    if num == 0:
        print('0! factorial is 1')
    elif num == 1:
        print('1! factorial is 1')
    else:
        # Loop element
        factorial_result = 1
        for i in range(2, num + 1):
            factorial_result = factorial_result * i
        print(f'{input_number}! factorial is {factorial_result}')

else:
    print('Not an integer number')
