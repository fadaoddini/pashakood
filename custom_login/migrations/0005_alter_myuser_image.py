# Generated by Django 4.2 on 2024-01-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_login', '0004_myuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_profile/str(uuid.uuid4())/'),
        ),
    ]
