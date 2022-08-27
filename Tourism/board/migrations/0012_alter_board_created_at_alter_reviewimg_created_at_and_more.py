# Generated by Django 4.0.6 on 2022-08-27 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_remove_reviewimg_user_reviewimg_board_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 18, 6, 41, 184740)),
        ),
        migrations.AlterField(
            model_name='reviewimg',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 18, 6, 41, 184740)),
        ),
        migrations.AlterField(
            model_name='reviewimg',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='Tourism/board/UploadImage'),
        ),
    ]
