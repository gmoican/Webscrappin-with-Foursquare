# Guillermo Moñino Cánovas
# Webscraping test with Foursquare API
# Process data and generate a CSV

import json
import csv


search_area = 'Valencia'

with open('4sq_data_' + search_area + '.json', 'r') as f:
    venues = json.load(f)


def process_4sq_venue(venue: dict):
    if 'locality' not in venue['location'] or 'address' not in venue['location']:
        return None
    #
    venueList = [venue['name'], '', '']
    #
    if 'price' in venue:
        priceDict = {'1': 'Cheap',
                     '2': 'Moderate',
                     '3': 'Expensive',
                     '4': 'Very expensive'}
        venueList.append(priceDict[str(venue['price'])])
    else:
        venueList.append('')
    #
    if 'rating' in venue:
        venueList.append(venue['rating'])
    else:
        venueList.append('')
    #
    # Fields for Google_place_ID and business_status
    venueList.extend(['', ''])
    #
    venueList.append(venue['location']['country'])
    #
    if 'admin_region' in venue['location']:
        venueList.append(venue['location']['admin_region'])
    elif 'region' in venue['location']:
        venueList.append(venue['location']['region'])
    else:
        venueList.append('')
    #
    venueList.extend([venue['location']['locality'], venue['location']['address']])
    #
    if 'postcode' in venue['location']:
        venueList.append(venue['location']['postcode'])
    else:
        venueList.append('')
    #
    venueList.extend([venue['geocodes']['main']['latitude'], venue['geocodes']['main']['longitude']])
    #
    # WEBSITE
    if 'website' in venue:
        venueList.append(venue['website'])
    else:
        venueList.append('')
    #
    # SOCIAL MEDIA
    if 'social_media' in venue:
        if 'facebook_id' in venue['social_media']:
            venueList.append('https://www.facebook.com/' + venue['social_media']['facebook_id'])
        else:
            venueList.append('')
        if 'instagram' in venue['social_media']:
            venueList.append('https://www.instagram.com/' + venue['social_media']['instagram'])
        else:
            venueList.append('')
    else:
        venueList.extend(['', ''])
    #
    # Youtube field
    venueList.append('')
    #
    venueType = ''
    for category in venue['categories']:
        venueType += category['name'] + ', '
    venueList.append(venueType[:-2])
    #
    if 'features' in venue and 'wheelchair_accesible' in venue['features']:
        venueList.append(venue['features']['wheelchair_accesible'])
    else:
        venueList.append('')
    # GENRE and COMPANY
    venueList.extend(['', ''])
    #
    if 'tel' in venue:
        venueList.append(venue['tel'])
    else:
        venueList.append('')
    #
    if 'email' in venue:
        venueList.append(venue['email'])
    else:
        venueList.append('')
    #
    if 'hours' in venue and 'display' in venue['hours']:
        venueList.append(venue['hours']['display'])
    else:
        venueList.append('')
    return venueList


# Process json file
results = {}
for venue in venues:
    # Visualize data with these prints
    print('\n--- --- ---')
    for key, val in venue.items():
        print(key, ' - ', val)
    if process_4sq_venue(venue):
        results[venue['name']] = process_4sq_venue(venue)

# Export list as a .csv file
with open('4sqList_' + search_area + '.csv', 'w') as f:
    write = csv.writer(f)
    for key, val in results.items():
        write.writerow(val)
