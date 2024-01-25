from django import forms

from custom_login import models


class RegisterUser(forms.ModelForm):
    class Meta:
        model = models.MyUser
        fields = ['mobile', ]
