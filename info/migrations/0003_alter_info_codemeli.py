# Generated by Django 3.2 on 2024-01-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_info_shaba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='codemeli',
            field=models.CharField(blank=True, max_length=24, null=True, unique=True),
        ),
    ]
