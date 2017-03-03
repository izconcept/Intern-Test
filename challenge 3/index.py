import json, urllib2


pokemonNumber = '25';

# Declaring headers + making GET request
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
pokemonRaw = json.load(opener.open('http://pokeapi.co/api/v2/pokemon/' + pokemonNumber))


# OPTIONAL: Cleaning up the return
pokemonClean = {}
pokemonClean['name'] = pokemonRaw['name']
pokemonClean['weight'] = pokemonRaw['weight']
pokemonClean['height'] = pokemonRaw['height']
pokemonClean['base_experience'] = pokemonRaw['base_experience']
pokemonClean['order'] = pokemonRaw['order']

pokemonClean['abilities'] = []
for ability in pokemonRaw['abilities']:
    pokemonClean['abilities'].append(ability['ability']['name'])

pokemonClean['stats'] = []
for stat in pokemonRaw['stats']:
    pokemonClean['stats'].append({stat['stat']['name'] : stat['base_stat']})

pokemonClean['items'] = []
for item in pokemonRaw['held_items']:
    pokemonClean['items'].append(item['item']['name'])

pokemonClean['moves'] = []
for move in pokemonRaw['moves']:
    pokemonClean['moves'].append(move['move']['name'])

pokemonClean['types'] = []
for type in pokemonRaw['types']:
    pokemonClean['types'].append(type['type']['name'])



# Put return in local JSON file so it's easier to manipulate later.
with open('pokemonClean.txt', 'w') as file:
    json.dump(pokemonClean, file, indent = 4)

with open('pokemonRaw.txt', 'w') as file:
    json.dump(pokemonRaw, file, indent=4)