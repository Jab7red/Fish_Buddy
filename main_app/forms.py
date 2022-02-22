from django.forms import ModelForm
from .models import Lake, Log

class LakeForm(ModelForm):
    class Meta:
        model = Lake
        fields = ['name']


class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ['date', 'location', 'length', 'weight']
        