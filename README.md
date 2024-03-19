# **Train Ticket Watcher**

An application that informs users about monitored international (or domestic) train ticket details.

### ***Current features***:
1. Gather and parse the required train ticket information using the official MÁV-START API
2. Create an endpoint (currently using Flask) with the gathered information that our services can use
3. Using our own endpoint, email users daily with the details of the cheapest tickets (currently the top two tickets per day, 14 days in advance)

### ***Planned features***:
- Create a heatmap calendar and include it in the daily emails
- Perform data analysis of the ticket information
- Add an endpoint that contains live information about trains we subscribe to

### ***The gathered information currently includes***:
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
