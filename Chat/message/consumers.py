import json
from channels.generic.websocket import WebsocketConsumer


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        print("Chat ID: ", self.chat_id)

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        print("Message received", message)

        self.send(text_data=json.dumps({'message': message}))