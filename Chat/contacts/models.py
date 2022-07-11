from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
"""class Contacts(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
"""


class Contacts(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_one")
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_two")