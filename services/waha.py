from dataclasses import dataclass
import requests


@dataclass
class Waha:
    url_waha: str = "http://waha:3000"


    def SendMessage(self, message, chat_id):
        link = self.url_waha + "/api/sendText"
        payload = {
        "chatId": chat_id,
        "reply_to": None,
        "text": message,
        "linkPreview": None,
        "linkPreviewHighQuality": None,
        "session": "default"
        }

        requests.post(link, json=payload)