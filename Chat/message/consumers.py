import json
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from .api.serializers import MessageSerializer
from asgiref.sync import async_to_sync


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.user = self.scope['user']
        self.chat_name = 'chat_'+str(self.chat_id)
        print(self.user)

        async_to_sync(self.channel_layer.group_add)(
            self.chat_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chat_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        action = text_data_json["action"]
        if action == "send_message":
            message = text_data_json["message"]
            new_message = Message.objects.create(content=message, author=self.user, idChat_id=self.chat_id)
            serialized_message = MessageSerializer(new_message)
    
            async_to_sync(self.channel_layer.group_send)(
                self.chat_name, {
                    'type': "send_message",
                    'message': serialized_message.data
                }
            )
            # self.send(text_data=json.dumps())
    
    def send_message(self, event):
        self.send(text_data=json.dumps(event))