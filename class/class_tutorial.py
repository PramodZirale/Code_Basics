virat = {
    'first_name': 'Virat',
    'last_name': 'Kohli',
    'role': 'Batsman',
    'birth_year': 1988,
    'scores': []
}

virat['scores'].append(45)
virat['scores'].append(78)
virat['scores'].append(12)
virat['scores'].append(8)

def get_age(player):
    # print(2021 - player['birth_year'])
    return 2021 - player['birth_year']

def get_avg_score(player):
    total = sum(player['scores'])
    # print(total)
    return total / len(player['scores'])

print(get_age(virat))
print(get_avg_score(virat))