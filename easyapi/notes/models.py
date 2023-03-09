from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    note = models.TextField()
    theme = models.CharField(max_length=255)
    pinned = models.BooleanField()
    owner = models.ForeignKey(
        User, related_name="leads", on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, related_name="notes", on_delete=models.CASCADE, null=True)

    REQUIRED_FIELDS = []
