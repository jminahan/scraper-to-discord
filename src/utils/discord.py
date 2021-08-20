import requests

class DiscordUtil:
    def __init__(self, channel):
        self.header = {

        }
        self.channel = channel

    def sendMessage(self, message):
        payload = {
            "content" : message
        }

        return requests.post(self.channel, data=payload, headers=self.header)

