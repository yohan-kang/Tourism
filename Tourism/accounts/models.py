from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters , validate_accommodation_link

class User(AbstractUser):
    nickname = models.CharField(
      max_length=15,
      unique=True, 
      null=True,
      validators=[validate_no_special_characters],
      error_messages={"unique": "This nickname is already in use"},
    )
  # only email login case 
  #   def __srt__(self):
  #       return self.email
class Review(models.Model):
    title = models.CharField(max_length=30)
    accommodation_name = models.CharField(max_length=20)
    accommodation_link = models.URLField( validators=[validate_accommodation_link])
    RATING_CHOICES = [
      (1, 1),
      (2, 2),
      (3, 3),
      (4, 4),
      (5, 5),
    ]
    rating =models.IntegerField(choices=RATING_CHOICES)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title