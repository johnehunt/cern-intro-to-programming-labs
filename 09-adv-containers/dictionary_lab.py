flights = {}

flights['London'] = ('EY123', 'Monday', '12:00', 'Geneva')
flights['Geneva'] = ('AI454', 'Tuesday', '13:00', 'London')
flights['Dublin'] = ('BA987', 'Wednesday', '14:00', 'Dublin')
flights['Seville'] = ('SA527', 'Thursday', '11:00', 'Cardiff')
flights['Cardiff'] = ('WA129', 'Friday', '10:00', 'Dublin')

print(f'Keys: {flights.keys()}')
print(f'values: {flights.values()}')
print()

print(f'The flight for Dublin is {flights.get("Dublin")}\n')

flights['France'] = ('AF429', 'Saturday', '09:00', 'London')

print(f'All key value pairs: {flights.items()}')

print('\nRemoving the Cardiff flight')
del flights['Cardiff']
print(f'All key value pairs: {flights.items()}')

