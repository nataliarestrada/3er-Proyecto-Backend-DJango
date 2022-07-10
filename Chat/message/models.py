from django.db import models

# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=120)
    #author
    sent = models.BooleanField(default=True)
    seen = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    # created_at = models.DateTimeField(default=datetime.now)
    # updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)