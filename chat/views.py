from channels.db import database_sync_to_async
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

from chat.models import Chat
from custom_login.models import MyUser


@login_required
def index_chat(request):
    context = dict()
    rooms = Chat.objects.all()
    context['rooms']= rooms
    return render(request, "chat/index.html", context)


@login_required
def room_chat(request, pk):
    context = dict()
    list_user_ok = list()
    mobile = request.user.mobile
    context['mobile'] = mark_safe(json.dumps(mobile))
    context['room_name'] = Chat.get_room_name(pk)
    context['room_pk'] = pk
    members = Chat.get_members(pk)
    context['members'] = members
    return render(request, "chat/chat.html", context)

