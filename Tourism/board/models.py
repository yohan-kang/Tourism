from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Board(models.Model):
    title = models.CharField(max_length=255,null=True)
    writer = models.ForeignKey(User, null=True,blank=True, on_delete=models.SET_NULL)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'myapp_board'

    def __str__(self) -> str:
      return self.writer.get_username()
        # return self.b_title + " " + self.b_writer + " " + self.accessUser.get_username()