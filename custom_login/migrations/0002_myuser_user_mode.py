# Generated by Django 4.2 on 2024-01-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_mode',
            field=models.BooleanField(choices=[(True, 'online'), (False, 'offline')], default=False),
        ),
    ]
