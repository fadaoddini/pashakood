from django.contrib import admin
from django.contrib.admin import register


from info.models import Info


@register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'user', 'shaba', 'codemeli', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('family', 'mobile', 'shaba', 'codemeli')
