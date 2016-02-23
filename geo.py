#get api key for google geolocation
import json
import googlemaps
import apitest

with open('auth.json') as credentials:
	data = json.load(credentials)

gmaps = googlemaps.Client(key=data['maps_api_key']) 

'''
make sure to create a function that appends 
(Boston, Ma) to the geolocation request.
also try and find a standard to normalize street numbers
of possible. Specifically in regards to how 
we deal with addresses with no numbers given
'''

'''
response scheme: 
geometry
place_id
formatted_address
address_components
types
'''

ticketsUrl = 'https://data.cityofboston.gov/resource/cpdb-ie6e.json' + '?$$app_token=' + data["api_key"]
# generate list of addresses
(rawAddr, formatted) = apitest.request(ticketsUrl)

def generateAddr(json_obj):
	return [elem['ticket_loc'] for elem in json_obj]

def locationQueryHelper(addr):
	queryAddr = addr + ', Boston, Ma'
	geocode_result = gmaps.geocode(queryAddr)
	return ((geocode_result[0]['address_components']), str(geocode_result[0]['geometry']['location_type']))

def locationQuery(addr_list):
	#extracts zip code from addresses that got tickets
	return [locationQueryHelper(ADDR_TICKETS[0])[0][len(locationQueryHelper(ADDR_TICKETS[0])[0])-1]['short_name'] for elem in addr_list if locationQueryHelper(elem)[1] != 'APPROXIMATE']

ADDR_TICKETS = generateAddr(rawAddr)
print(locationQuery(ADDR_TICKETS[900:950]))







