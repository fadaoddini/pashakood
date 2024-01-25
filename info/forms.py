from django import forms
from django.core.exceptions import ValidationError

from info.models import Info
from lib.validators import check_shaba_validator


class InfoUserForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'family', 'shaba', 'image_shaba', 'codemeli', 'image_codemeli']
        # exclude = ['user', 'is_active']

    # def clean_shaba(self):
    #     shaba = self.cleaned_data['shaba']
    #
    #     if len(shaba) != 24:
    #         raise ValidationError("شماره شبا وارد شده معتبر نیست")
    #     return shaba

    # def clean_codemeli(self):
    #     codemeli = self.cleaned_data['codemeli']
    #
    #     if len(codemeli) != 10:
    #         raise ValidationError("کد ملی وارد شده معتبر نیست")
    #     return codemeli


class InfoImageForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['image']
