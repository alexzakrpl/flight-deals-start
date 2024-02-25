import requests
import datetime as dt
import os
# import json

HOME_CITY = 'BER'
PERIOD_TO_SEARCH = 180
NIGHTS_IN_PLACE = {
    'min': 2,
    'max': 10
}

KIWI_ENDPOINT = 'https://api.tequila.kiwi.com/v2/search'
KIWI_API = os.getenv('KIWI_API')

HEADERS = {
    'apikey': KIWI_API
}


class FlightSearch:
    def __init__(self, conditions: tuple) -> None:
        self.home_city = HOME_CITY
        self.to_city = conditions[0]

        date_from, date_to = self._date()

        self.params = {
            'fly_from': self.home_city,
            'fly_to': self.to_city,
            'date_from': date_from,
            'date_to': date_to,
            'return_from': date_from,
            'return_to': date_to,
            'nights_in_dst_from': NIGHTS_IN_PLACE['min'],
            'nights_in_dst_to': NIGHTS_IN_PLACE['max'],
            'price_from': 1,
            'price_to': conditions[1],
            'curr': 'EUR'
        }

        self.response_data = self._response(self.params)
        self.ticket_is_exist = self.__check_existence(self.response_data)

        # print(params)

    def _date(self):
        date_from = dt.date.today().strftime('%d/%m/%Y')
        date_to = (dt.date.today() +
                   dt.timedelta(days=PERIOD_TO_SEARCH)).strftime('%d/%m/%Y')

        return date_from, date_to

    def _response(self, params):
        response = requests.get(url=KIWI_ENDPOINT,
                                headers=HEADERS,
                                params=params)

        print(response.status_code)
        # print(response.text)
        # print(f'Params = {params}')

        response_json = response.json()

        # for test
        # with open('kiwi.json', mode='w') as f:
        #     # json.dump(response_json['data'][0], f)
        #     json.dump(response_json, f)

        return response_json

    def __check_existence(self, response):
        if len(response['data']) != 0:
            return True
        else:
            return False
