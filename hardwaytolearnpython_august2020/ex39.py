states = {
    'Россия': 'RU',
    'Германия': 'DE',
    'Узбекистан': 'UZ',
    'Зимбабве': 'ZW',
    'Турция': 'TR'
}

cities = {
    'UZ': 'Газли',
    'TR': 'Сарыгерме',
    'DE': 'Мюнхен'
}

cities['ZW'] = 'Гверу'
cities['UA'] = 'Днепр'

print('-'*10)
print(f" В стране ZW есть { cities['ZW'] }")
print(f" В стране UA есть { cities['UA'] }")
print('-'*10)
for state, abbr in list(states.items()):
    print(f"{state} - {abbr}")
print('-'*10)
for city, abbr in list(cities.items()):
    print(f"{city} - {abbr}")
print('-'*10)
for state, abbr in list(states.items()):
    print(f"{state} - {abbr}")
    print(f'{cities[abbr]}')
