from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=15,unique=True , null=True)
    pass
  # only email login case 
  #   def __srt__(self):
  #       return self.email
