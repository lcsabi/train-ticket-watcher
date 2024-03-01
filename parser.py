import json

import requests
from requests import Response

import config

url = config.endpoint
headers = config.headers
data = config.payload
response: Response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    try:
        raw_response: dict = response.json()['route']
        parsed_response = dict()
        offers_list = list()

        # Offer information
        for offer in raw_response:
            current_offer_dict = dict()
            tickets = offer['details']['tickets']
            current_offer_dict['tickets'] = list()

            # Ticket information
            for ticket in tickets:
                current_ticket_dict = dict()
                current_ticket_dict['full_price_huf'] = ticket['grossPrice']['amountInDefaultCurrency']
                current_ticket_dict['full_price_eur'] = ticket['grossPrice']['amount']
                current_ticket_dict['discounted_price_huf'] = ticket['discountedGrossPrice']['amountInDefaultCurrency']
                current_ticket_dict['discounted_price_eur'] = ticket['discountedGrossPrice']['amount']
                current_ticket_dict['number_of_stops'] = len(ticket['touchedStations'])
                current_ticket_dict['names_of_stops'] = [station['name'] for station in ticket['touchedStations'] if station['name']]
                current_ticket_dict['offer_valid_until'] = ' '.join(ticket['offerValidTo'].split('+')[0].split('T'))
                current_offer_dict['tickets'].append(current_ticket_dict)

            # Offer details
            current_details_dict = dict()
            current_details_dict['transfers'] = offer['transfersCount']
            current_details_dict['departure_time'] = ' '.join(offer['departure']['time'].split('+')[0].split('T'))
            current_details_dict['arrival_time'] = ' '.join(offer['arrival']['time'].split('+')[0].split('T'))
            current_details_dict['total_travel_time'] = offer['travelTimeMin']
            current_offer_dict['details'] = current_details_dict

            # Routes information
            routes = offer['details']['routes']
            current_offer_dict['routes'] = list()
            for route in routes:
                current_route_dict = dict()
                current_route_dict['start_station_name'] = route['startStation']['name']
                current_route_dict['departure_time'] = ' '.join(route['departure']['time'].split('+')[0].split('T'))
                current_route_dict['destination_station_name'] = route['destionationStation']['name']
                current_route_dict['arrival_time'] = route['destionationStation']['arrivalTime']
                current_route_dict['distance_in_km'] = route['distance']
                current_route_dict['train_number'] = route['trainDetails']['trainNumber']
                current_route_dict['train_name'] = route['trainDetails']['trainKind']['name']
                current_offer_dict['routes'].append(current_route_dict)

            offers_list.append(current_offer_dict)

        parsed_response['offers'] = offers_list
        print(parsed_response)
    except json.decoder.JSONDecodeError:
        print("Failed to parse JSON response.")
else:
    print("Request unsuccessful:", response.status_code)
    print(response.text)

# Get tickets for 16 days in advance
# Top 2 tickets / day
