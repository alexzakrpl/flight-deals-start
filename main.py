from dotenv import load_dotenv
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager

load_dotenv()

flight_conditions = DataManager()

for goal in flight_conditions.goals:

    search = FlightSearch(goal)

    if search.ticket_is_exist:
        search_result = FlightData(search)
        msg = NotificationManager(search_result.ticket_data)
        msg.send_alarm(msg.msg)
