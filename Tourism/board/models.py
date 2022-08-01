from django.db import models

class Board(models.Model):
    b_title = models.CharField(db_column='b_title', max_length=255)
    b_writer = models.CharField(db_column='b_writer', max_length=50)
    b_date = models.DateTimeField(db_column='b_date', )

    class Meta:
        managed = False
        db_table = 'myapp_board'