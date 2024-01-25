from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model as user_model


class Info(models.Model):
    ACTIVE = True
    INACTIVE = False

    STATUS_INFO = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
    )
    TAEED = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
    )
    User = user_model()
    name = models.CharField(max_length=32)
    family = models.CharField(max_length=32)
    image = models.ImageField(upload_to='%Y/%m/%d/users/', null=True, blank=True)
    shaba = models.CharField(max_length=24, unique=True, null=True, blank=True)
    image_shaba = models.ImageField(upload_to='%Y/%m/%d/shabas/', null=True, blank=True)
    codemeli = models.CharField(max_length=24, unique=True, null=True, blank=True)
    okmeli = models.BooleanField(choices=TAEED, default=INACTIVE)
    okbank = models.BooleanField(choices=TAEED, default=INACTIVE)
    image_codemeli = models.ImageField(upload_to='%Y/%m/%d/codemelis/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info', null=True,
                                blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(choices=STATUS_INFO, default=INACTIVE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)