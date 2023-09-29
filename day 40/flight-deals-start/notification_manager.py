
from twilio.rest import Client



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.account_sid = 'AC39358c6549c0c23255ad4b099145ad6e'
        self.auth_token = '89c01506d5574a7e21dd7e40fb622bb7'



    def send_msg(self,msg):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
                from_='+12565136259',
                body=msg,
                to='+9779846884101'
                )

        print(message.sid)