# Guillermo Moñino Cánovas
# Webscraping test with Foursquare API
# Retrieve data and generate a JSON

import json
import requests

API_key = 'your key here'
search_area = 'Valencia'

'''
Use coordinates when 'search_area' may point to ambiguous locations
Leave coordinates commented when you don't need them
# EXAMPLE OF AMBIGUOUS LOCATION
I was interested in retrieving venues from Cartagena, Murcia
If I just type search_area = 'Cartagena', the results are from Cartagena, Colombia
In this case, it's better to pass the API the longitude/latitude coordinates
'''
# coordinates = '37.615665%2C-0.989313'

categories = {'DanceHall': '10013',
              # 'PerformingArts': '10035',
              'Amphitheater': '10036',
              'ConcertHall': '10037',
              'IndieTheater': '10038',
              'MusicVenue': '10039',
              'JazzBluesVenue': '10040',
              'RockClub': '10041',
              'OperaHouse': '10042',
              'Theater': '10043',
              # 'Bar': '13003',
              'BeachBar': '13005',
              'CocktailBar': '13009',
              'KaraokeBar': '13015',
              'PianoBar': '13017',
              'Pub': '13018',
              'Rooftop Bar': '13019',
              'MusicFestival': '14005'}

# PART1: Broad search for venues in an area
headers = {
    "accept": "application/json",
    "Authorization": API_key
}

results = []
for key, value in categories.items():
    if 'coordinates' in globals():
        url = "https://api.foursquare.com/v3/places/search?ll=" + coordinates + "&categories=" + value + "&fields=name%2Cgeocodes%2Clocation%2Ccategories%2Clink%2Ctel%2Cemail%2Cwebsite%2Csocial_media%2Chours%2Crating%2Cprice%2Cprice%2Cfeatures%2C&limit=50"
    else:
        url = "https://api.foursquare.com/v3/places/search?categories=" + value + "&fields=name%2Cgeocodes%2Clocation%2Ccategories%2Clink%2Ctel%2Cemail%2Cwebsite%2Csocial_media%2Chours%2Crating%2Cprice%2Cfeatures%2C&near=" + search_area + '&limit=50'

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    results.extend(data['results'])

for venue in results:
    print('\n--- --- ---')
    for key, val in venue.items():
        print(key, ' - ', val)

print(len(results))

# Dump data
with open('4sq_data_' + search_area + '.json', 'w') as f:
    json.dump(results, f)
