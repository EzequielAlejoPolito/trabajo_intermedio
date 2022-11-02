from unicodedata import name
from django import forms

from my_app.models import Dato


class DatoFormulario(forms.Form):
    
    rol = forms.CharField()
    name = forms.CharField()
    last_name = forms.CharField()