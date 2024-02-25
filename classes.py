from typing import List


class Ticket:
    def __init__(self, ticket_response: dict):
        self.full_ticket_price_eur = ticket_response["grossPrice"]["amount"]
        self.full_ticket_price_huf = ticket_response["grossPrice"]["amountInDefaultCurrency"]
        self.discounted_ticket_price_huf = ticket_response["discountedGrossPrice"]["amountInDefaultCurrency"]
        self.discounted_ticket_price_eur = ticket_response["discountedGrossPrice"]["amount"]
        self.stops = [station["name"] for station in ticket_response["touchedStations"] if station["name"]]
        self.valid_until = " | ".join(ticket_response["offerValidTo"].split("+")[0].split("T"))

    def __repr__(self):
        return ("Full price: " + str(self.full_ticket_price_eur) + " EUR / "
                + str(self.full_ticket_price_huf) + " HUF"
                + (("\nDiscounted price: " + str(self.discounted_ticket_price_eur)) if (self.discounted_ticket_price_eur < self.full_ticket_price_eur) else "")
                + "\n" + str(len(self.stops)) + " Stops: " + " - ".join(self.stops)
                + "\nOffer valid until: " + self.valid_until)


class Route:
    pass


class Offer:
    def __init__(self, offer_response: dict):
        self.departure_time = " | ".join(offer_response["departure"]["time"].split("+")[0].split("T"))
        self.arrival_time = " | ".join(offer_response["arrival"]["time"].split("+")[0].split("T"))
        self.transfer_count = offer_response["transfersCount"]
        self.total_travel_time = offer_response["travelTimeMin"]
        self.tickets: List[Ticket] = []
        self.routes: List[Route] = []

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)

    def add_route(self, route: Route):
        self.routes.append(route)

    def __repr__(self):
        # TODO: Add start and end stations to repr, create station code mapping
        string_repr = "*" * 40 + "\n"
        for ticket in self.tickets:
            string_repr += str(ticket)

        string_repr += "\nNumber of transfers: " + str(self.transfer_count)
        string_repr += "\nDeparture time: " + str(self.departure_time)
        string_repr += "\nArrival time: " + str(self.arrival_time)
        string_repr += "\nTotal travel time (HH:MM): " + str(self.total_travel_time)
        string_repr += "\n" + "*" * 40

        return string_repr
