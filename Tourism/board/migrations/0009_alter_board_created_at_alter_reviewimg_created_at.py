# Generated by Django 4.0.6 on 2022-08-26 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_alter_board_created_at_alter_reviewimg_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 10, 16, 11, 609388)),
        ),
        migrations.AlterField(
            model_name='reviewimg',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 10, 16, 11, 610393)),
        ),
    ]
