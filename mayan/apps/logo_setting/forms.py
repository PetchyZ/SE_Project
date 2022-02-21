from django import forms

from .models import LogoName


class ThemeForm(forms.ModelForm):
    class Meta:
        fields = ('logoName', )
        model = LogoName
