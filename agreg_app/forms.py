from django import forms
from .models import Values


class LookValue(forms.Form):
    date = forms.DateField()

