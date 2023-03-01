import csv

transactions = (
        ('deposit', 10.05),
        ('deposit', 23.45),
        ('withdraw', 12.33),
        ('withdraw', 5.00)
)


def write_account_transaction_to_csv(filename, data):
    print('Starting write of dict CSV example')
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['transaction_type', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # Write out the transactions
        for transaction in data:
            writer.writerow({'transaction_type': transaction[0],
                             'amount': transaction[1]})


print('Starting')

print('Writing Account Transactions')
write_account_transaction_to_csv('accounts.csv', transactions)

print('Done')
