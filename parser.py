import json
from typing import List

import requests
from requests import Response

import config
from classes import Ticket, Offer

url = config.endpoint
headers = config.headers
data = config.payload
response: Response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    try:
        parsed_response: dict = response.json()
        offers_response: dict = parsed_response["route"]
        all_offers: List[Offer] = []

        for offer in offers_response:
            if offer["transfersCount"] > 1:
                continue
            offer_object: Offer = Offer(offer)
            tickets_response: dict = offer["details"]["tickets"]
            for ticket in tickets_response:
                ticket_object: Ticket = Ticket(ticket)
                offer_object.add_ticket(ticket_object)

            all_offers.append(offer_object)

            routes: dict = offer["details"]["routes"]

        # TODO: Implement sorting logic for offers based on ticket prices
        # sorted_offers = sorted(all_offers, key=lambda x: min(lambda y: x.tickets))
        # print(sorted_offers)
        print(all_offers)
    except json.decoder.JSONDecodeError:
        print("Failed to parse JSON response.")
else:
    print("Request unsuccessful:", response.status_code)
    print(response.text)

# Get tickets for 16 days in advance
# Top 2 tickets / day
