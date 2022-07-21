# CRUD
# retrieve, create, update, destroy
from xml.etree.ElementTree import tostring
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Message
from django.contrib.auth import get_user_model
from .api.serializers import MessageSerializer

from django.shortcuts import render
User = get_user_model()

def conversation(request):
    msj = Message.objects.filter(idChat=4)
    user=request.user
    return render(request, "conversation.html",{
        'user': user,
        'conversation': msj 
    })

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
