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

### 3. Configuration file
