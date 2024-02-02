import json

import requests

import configuration

url = configuration.endpoint
headers = configuration.headers
data = configuration.payload

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Request successful.")
    try:
        parsed_response = response.json()
        offers = parsed_response["route"]
        for offer in offers:
            tickets = offer["details"]["tickets"]
            routes = offer["details"]["routes"]
            for ticket in tickets:
                print(ticket["grossPrice"]["amountInDefaultCurrency"])
    except json.decoder.JSONDecodeError:
        print("Failed to parse JSON response.")
else:
    print("Request unsuccessful:", response.status_code)
    print(response.text)
