from django import forms
from .models import Subscriber


class NoPageSendingForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = ['']
