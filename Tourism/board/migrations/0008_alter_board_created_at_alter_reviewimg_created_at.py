# Generated by Django 4.0.6 on 2022-08-25 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_alter_board_created_at_reviewimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 25, 16, 53, 9, 990029)),
        ),
        migrations.AlterField(
            model_name='reviewimg',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 25, 16, 53, 9, 990529)),
        ),
    ]
