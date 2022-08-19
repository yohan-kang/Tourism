from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Board(models.Model):
    b_title = models.CharField(db_column='b_title', max_length=255)
    b_writer = models.CharField(db_column='b_writer', max_length=50)
    b_date = models.DateTimeField(db_column='b_date')
    accessUser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = True
        db_table = 'myapp_board'