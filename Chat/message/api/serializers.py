from rest_framework import serializers

from ..models import Message, User


class Author(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class MessageSerializer(serializers.ModelSerializer):
    author = Author(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'content', 'sent', 'seen', 'deleted', 'created_at', 'updated_at', 'author', 'idChat']