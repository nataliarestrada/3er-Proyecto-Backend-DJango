from rest_framework import serializers
from ..models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'sent', 'seen', 'deleted', 'created_at', 'updated_at']