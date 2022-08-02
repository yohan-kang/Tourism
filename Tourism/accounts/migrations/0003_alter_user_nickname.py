# Generated by Django 4.0.6 on 2022-08-01 04:30

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': 'This nickname is already in use'}, max_length=15, null=True, unique=True, validators=[accounts.validators.validate_no_special_characters]),
        ),
    ]