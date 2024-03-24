# **Train Ticket Watcher**

### 1. Description
An application that informs users about monitored international (or domestic) train ticket details.

#### 1.1 Current features
1. Gather and parse the required train ticket information using the official MÁV-START API
2. Create an endpoint (currently using Flask) with the gathered information that our services can use
3. Using our own endpoint, email users daily with the details of the cheapest tickets (currently the top two tickets per day, 14 days in advance)

#### 1.2 Planned features
- Create subscription feature for users, so they can register to the train lines they are interested in:
  - Users email the bot which sends a POST request to our API that the mail service handles
  - Will require a database (probably go with SQL)
- Caching of third-party API response
- Perform data analysis of the ticket information and create a heatmap calendar to include in the daily emails
- Add an endpoint that contains live information about trains users subscribe to

#### 1.3 The gathered information currently includes:
- Departure/arrival station and time
- Total travel time
- Number of transfers and name of transfer stations
- Ticket price, discounts if applicable
- Number and name of stops
- Details about every route in the journey:
  - Departure/arrival station and time
  - Train name and number
  - Travel distance
  - Planned: live data such as track number, delays

### 2. Documentation
#### IMPORTANT: The server has to be running for the mail service to work.

#### 2.1 Endpoints
Every endpoint can be accessed via ***/api/v1***
##### 2.1.1 /offers [GET]
Description of the endpoint will come here.
##### 2.1.1.1 Example response
Singular offer
```json
{
  "offers": [
    {
      "details": {
        "from": "Würzburg Hbf",
        "to": "Budapest-Keleti",
        "transfers": 1,
        "transfer_stations": ["Linz Hbf"],
        "departure_time": "2024-03-30 07:34:00",
        "arrival_time": "2024-03-30 16:19:00",
        "total_travel_time": "08:45"
      },
      "tickets": [
        {
          "full_price_huf": 25840,
          "full_price_eur": 68,
          "discounted_price_huf": 25840,
          "discounted_price_eur": 68,
          "number_of_stops": 12,
          "names_of_stops": ["Fürth(Bay)Hbf", "Steinach(B Rothenb)", "Ansbach", "Nürnberg Hbf", "Regensburg Hbf", "Passau Hbf", "Wels Hbf", "Bécs Főpályaudvar (Wien Hbf)", "Bruck/Leitha", "Hegyeshalom(Gr)", "Győr", "Budapest-Keleti"],
          "offer_valid_until": "2024-03-31 23:59:59"
        }
      ],
      "routes": [
        {
          "start_station_name": "Würzburg Hbf",
          "departure_time": "2024-03-30 07:34:00",
          "destination_station_name": "Linz Hbf",
          "arrival_time": "11:26",
          "distance_in_km": 433,
          "train_number": "21",
          "train_name": "ICE"
        },
        {
          "start_station_name": "Linz Hbf",
          "departure_time": "2024-03-30 12:17:00",
          "destination_station_name": "Budapest-Keleti",
          "arrival_time": "16:19",
          "distance_in_km": 466,
          "train_number": "63",
          "train_name": "railjet xpress"
        }
      ]
    }
  ]
}
```
### 4. Templates
