from datetime import datetime
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Board(models.Model):
    title = models.CharField(max_length=255,null=True)
    writer = models.ForeignKey(User, null=True,blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("locations.Location", null=True,blank=True, on_delete=models.SET_NULL)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'myapp_board'

    # def __str__(self) -> str:
    #   return self.writer.get_username()  + " " + self.title
      # return self.writer.get_username()
        # return self.b_title + " " + self.b_writer + " " + self.accessUser.get_username()

class ReviewImg(models.Model):
    board = models.ForeignKey(Board, null=True,blank=True, on_delete=models.SET_NULL)
    image_name = models.CharField(null=True,max_length=200)
    image_url = models.ImageField(upload_to='',blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)

