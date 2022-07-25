from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters

class User(AbstractUser):
    nickname = models.CharField(
      max_length=15,
      unique=True, 
      null=True,
      validators=[validate_no_special_characters],
      error_messages={"unique": "This nickname is already in use"},
    )
    pass
  # only email login case 
  #   def __srt__(self):
  #       return self.email
