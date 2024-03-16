import json
from typing import List

import requests
from requests import Response

import config


class OfferParser:
    @staticmethod
    def parse_offer(raw_offer_dict) -> dict:
        current_offer_dict = {
            'details': OfferParser.parse_offer_details(raw_offer_dict),
            'tickets': OfferParser.parse_offer_tickets(raw_offer_dict['details']['tickets']),
            'routes': OfferParser.parse_offer_routes(raw_offer_dict['details']['routes'])
        }
        return current_offer_dict

    @staticmethod
    def parse_offer_details(raw_details_dict: dict) -> dict:
        parsed_details = {
            'from': raw_details_dict['details']['routes'][0]['startStation']['name'],
            'to': raw_details_dict['lastStation'],
            'transfers': raw_details_dict['transfersCount'],
            'departure_time': ' '.join(raw_details_dict['departure']['time'].split('+')[0].split('T')),
            'arrival_time': ' '.join(raw_details_dict['arrival']['time'].split('+')[0].split('T')),
            'total_travel_time': raw_details_dict['travelTimeMin']
        }
        return parsed_details

    @staticmethod
    def parse_offer_tickets(raw_tickets_list: List[dict]) -> List[dict]:
        parsed_tickets = []
        for ticket in raw_tickets_list:
            current_ticket_dict = {
                'full_price_huf': ticket['grossPrice']['amountInDefaultCurrency'],
                'full_price_eur': ticket['grossPrice']['amount'],
                'discounted_price_huf': ticket['discountedGrossPrice']['amountInDefaultCurrency'],
                'discounted_price_eur': ticket['discountedGrossPrice']['amount'],
                'number_of_stops': len(ticket['touchedStations']),
                'names_of_stops': [station['name'] for station in ticket['touchedStations'] if station['name']] + [ticket['endStation']['name']],
                'offer_valid_until': ' '.join(ticket['offerValidTo'].split('+')[0].split('T'))
            }
            parsed_tickets.append(current_ticket_dict)
        return parsed_tickets

    @staticmethod
    def parse_offer_routes(raw_routes_list: List[dict]) -> List[dict]:
        parsed_routes = []
        for route in raw_routes_list:
            current_route_dict = {
                'start_station_name': route['startStation']['name'],
                'departure_time': ' '.join(route['departure']['time'].split('+')[0].split('T')),
                'destination_station_name': route['destionationStation']['name'],
                'arrival_time': route['destionationStation']['arrivalTime'],
                'distance_in_km': route['distance'],
                'train_number': route['trainDetails']['trainNumber'],
                'train_name': route['trainDetails']['trainKind']['name']
            }
            parsed_routes.append(current_route_dict)
        return parsed_routes

    @staticmethod
    def parse_response(response_json: Response):
        parsed_response = {'offers': []}
        for offer in response_json:
            current_offer = OfferParser.parse_offer(offer)
            parsed_response['offers'].append(current_offer)
        return parsed_response


# TODO: change POST request format
url = config.endpoint
headers = config.headers
data = config.payload
response: Response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    try:
        raw_response = response.json()
        parsed = OfferParser.parse_response(raw_response['route'])
        print(parsed)
    except json.decoder.JSONDecodeError:
        print("Failed to parse JSON response.")
else:
    print("Request unsuccessful:", response.status_code)
    print(response.text)

# Get tickets for 16 days in advance
# Top 2 tickets / day
