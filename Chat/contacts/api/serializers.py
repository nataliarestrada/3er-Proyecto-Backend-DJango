from rest_framework import serializers
from ..models import Contacts, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class ContactsSerializer(serializers.ModelSerializer):
    user_one = UserSerializer(read_only=True)
    user_two = UserSerializer(read_only=True)

    class Meta:
        model = Contacts
        fields = ['id', 'user_one', 'user_two']