# Generated by Django 4.0.6 on 2022-08-27 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_alter_board_created_at_alter_reviewimg_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 18, 16, 2, 431125)),
        ),
        migrations.AlterField(
            model_name='reviewimg',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 18, 16, 2, 431567)),
        ),
        migrations.AlterField(
            model_name='reviewimg',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
