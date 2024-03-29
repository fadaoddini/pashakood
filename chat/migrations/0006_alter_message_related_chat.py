# Generated by Django 4.2 on 2024-01-09 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_chat_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='related_chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='chat.chat'),
        ),
    ]
