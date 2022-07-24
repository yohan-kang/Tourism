from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
  # only email login case 
  #   def __srt__(self):
  #       return self.email
