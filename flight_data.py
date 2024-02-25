from flight_search import FlightSearch
from ticket_data import TicketData

flight_data_structure = {
        "cityFrom": "",
        "cityCodeFrom": "",
        "local_departure": ""
        }

# This class is responsible for structuring the flight data.


class FlightData:
    def __init__(self, flight_search: FlightSearch) -> None:
        self._flight_search = flight_search
        data = self._flight_search.response_data
        self.ticket_data = self.__validate_flight_data(
            self.__check_flights(data))

    def __check_flights(self, data):

        flight_data = {}
        flight_route = data['data'][0]["route"]

        for route in flight_route:
            if route["cityCodeFrom"] == self._flight_search.home_city:
                for key in flight_data_structure.keys():
                    from_key = f'from_{key}'
                    flight_data[from_key] = route[key]

            elif route["cityCodeFrom"] == self._flight_search.to_city:
                for key in flight_data_structure.keys():
                    to_key = f'to_{key}'
                    flight_data[to_key] = route[key]

        flight_data["nightsInDest"] = data['data'][0]["nightsInDest"]
        flight_data["price"] = data['data'][0]["price"]

        # print(f'__check_flights: \n {flight_data} \n')

        return flight_data

    def __validate_flight_data(self, flight_data: dict):
        validated_flight_data = TicketData(**flight_data)
        return validated_flight_data
