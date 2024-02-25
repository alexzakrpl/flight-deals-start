import gspread

CREDENTIALS = 'gspread.json'
WORKSHEET = "Flight Deals"
SHEET = "prices"
CODS_CITY_TO = 'IATA Code'
GOAL_PRICES = 'Lowest Price'


class DataManager:
    def __init__(self) -> None:
        self.goals = self.__get_goals()

    def __get_goals(self) -> list:
        gc = gspread.service_account(filename=CREDENTIALS)
        sh = gc.open(WORKSHEET)
        worksheet = sh.worksheet(SHEET)
        list_of_dicts = worksheet.get_all_records()

        flight_goals = [(item[CODS_CITY_TO], item[GOAL_PRICES])
                        for item in list_of_dicts]
        return flight_goals
