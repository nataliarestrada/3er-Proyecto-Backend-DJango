from django.urls import re_path
from .consumers import MessageConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chat_id>\d+)$', MessageConsumer.as_asgi())
]