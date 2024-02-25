import os
from ticket_data import TicketData
from twilio.rest import Client

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')


class NotificationManager:
    def __init__(self, ticket_data: TicketData) -> None:
        self.ticket_data = ticket_data

        fight_data_dict = {

            'from_cityFrom': self.ticket_data.from_cityFrom,
            'from_cityCodeFrom': self.ticket_data.from_cityCodeFrom,
            'from_local_departure': (self.ticket_data.from_local_departure
                                     .strftime('%d/%m/%Y %H:%M')),

            'to_cityFrom': self.ticket_data.to_cityFrom,
            'to_cityCodeFrom': self.ticket_data.to_cityCodeFrom,
            'to_local_departure': (self.ticket_data.to_local_departure
                                   .strftime('%d/%m/%Y %H:%M')),

            'nightsInDest': self.ticket_data.nightsInDest,
            'price': self.ticket_data.price
            }

        # print(f'sms dict: {fight_data_dict} \n\n')

        self.msg = self.__create_msg_text(fight_data_dict)

    def __create_msg_text(self, fd: dict) -> str:

        msg = (f"Low price alert! Only {fd['price']} EUR to fly from "
               f"{fd['from_cityFrom']}-{fd['from_cityCodeFrom']} to "
               f"{fd['to_cityFrom']}-{fd['to_cityCodeFrom']}, from "
               f"{fd['from_local_departure']} to {fd['to_local_departure']}."
               )
        return msg

    def send_alarm(self, msg):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(from_='+16593992789',
                                         body=msg,
                                         to='+48789741591')

        print(message.status)
