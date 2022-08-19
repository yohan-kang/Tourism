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

    def __str__(self) -> str:
        return super().__str__()
  # only email login case 
  #   def __srt__(self):
  #       return self.email

# ex)
# class Note(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#   body = models.TextField()