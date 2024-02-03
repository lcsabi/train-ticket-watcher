import json

import requests

import config
from classes import Ticket, Offer

url = config.endpoint
headers = config.headers
data = config.payload
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    try:
        parsed_response = response.json()
        offers_response = parsed_response["route"]
        all_offers = []

        for offer in offers_response:
            offer_object = Offer(offer)
            tickets_response = offer["details"]["tickets"]
            for ticket in tickets_response:
                ticket_object = Ticket(ticket)
                offer_object.add_ticket(ticket_object)

            all_offers.append(offer_object)
            print(offer_object)

            routes = offer["details"]["routes"]
    except json.decoder.JSONDecodeError:
        print("Failed to parse JSON response.")
else:
    print("Request unsuccessful:", response.status_code)
    print(response.text)
