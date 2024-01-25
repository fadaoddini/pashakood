import jdatetime
from rest_framework import serializers

from chat.models import Message, Chat
from lib.jalalidate import MiladiToJalali


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['pk', 'room_name', 'members']


class MessageSerializer(serializers.ModelSerializer):
    time_persian = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['__str__', 'content', 'timestamp', 'time_persian']

    def get_time_persian(self, obj):
        new_time = str(obj.author.last_time_online)
        name_user = obj.author.first_name + " " + obj.author.last_name
        result = MiladiToJalali.to_jalali_serializer(new_time)

        return result + " ( " + name_user + " ) "

