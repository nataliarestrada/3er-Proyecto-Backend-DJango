# CRUD
# retrieve, create, update, destroy
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Message
from .api.serializers import MessageSerializer

from django.shortcuts import render

def home(request):
    return render(request, "home.html")


# Create your views here.
# Lista todos los elementos de mensajes
class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Lista solo un elemento o registro
class MessageDetailView(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Crea un mensaje
class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Actualiza un mensaje
class MessageUpdateView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Eliminar un mensaje
class MessageDeleteView(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
