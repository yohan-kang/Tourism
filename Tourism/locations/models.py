from django.db import models
from datetime import datetime
from django.conf import settings
# User = settings.AUTH_USER_MODEL
class Location(models.Model):
    class Type(models.IntegerChoices):
        State=1
        District=2
        City=3
        CHC=4
    name_of_place = models.CharField(null=True,max_length=150)
    type = models.IntegerField(null=True,choices=Type.choices)
    parent_location = models.ForeignKey("self", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)

