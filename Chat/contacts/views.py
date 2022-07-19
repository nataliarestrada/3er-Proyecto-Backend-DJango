from rest_framework.viewsets import ModelViewSet
from .api.serializers import ContactsSerializer, Contacts, User
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
# Create your views here.
# from django.conf import settings
# import redis
# r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

def mychats(request):
    chats = Contacts.objects.filter(user_one=request.user.id)
    return render(request, "mychats.html",{
        'mychats': chats
    })

class ContactsViewSet(ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    authentication_classes = (SessionAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    # Sobrescribir los métodos
    def list(self, request, *args, **kwargs):
        queryset = Contacts.objects.filter(user_one=request.user.id)
        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Contacts.objects.all()
        contact = get_object_or_404(queryset, pk=pk)
        if contact.user_one.id == request.user.id:
            serializer = ContactsSerializer(contact)
            return Response(serializer.data)
        else:
            return Response(status=404)

    def create(self, request, *args, **kwargs):
        try:
            user = request.user.id
            user2 = request.data["user_two"]
            contact, _ = Contacts.objects.get_or_create(user_one_id=user, user_two_id=user2)
            serializer = ContactsSerializer(contact)
            return Response(serializer.data)
        except:
            return Response({
                "success": False,
                "message": "Verify user ids"
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            contact = self.get_object()
            print(contact.user_one.id)
            if contact.user_one.id == request.user.id:
                self.perform_destroy(contact)
        except:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)