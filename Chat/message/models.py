from django.db import models
from django.contrib.auth import get_user_model
from contacts.models import Contacts
User = get_user_model()


# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=120)
    sent = models.BooleanField(default=True)
    seen = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    idChat = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(default=datetime.now)
    # updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)