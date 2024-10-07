import requests
import os
from dotenv import load_dotenv

load_dotenv()

class SendMessage():
    def __init__(self):        
        #Getting Env Variables
        self.DEVICE_ID = str(os.getenv('DEVICE_ID'))
        self.INTEGRATION_TOKEN = str(os.getenv('INTEGRATION_TOKEN'))
        self.SECURITY_TOKEN = str(os.getenv('SECURITY_TOKEN'))

    def send_message(self, number, message):

        url = f"https://api.z-api.io/instances/{self.DEVICE_ID}/token/{self.INTEGRATION_TOKEN}/send-text"
        headers = {
            "Client-Token": self.SECURITY_TOKEN
        }
        body = {
            "phone": number,
            "message": message
        }

        response = requests.post(url=url, headers=headers, data=body)
        print(f'Response: {response.status_code}')
        print(f'Response: {response.json()}')
        return response