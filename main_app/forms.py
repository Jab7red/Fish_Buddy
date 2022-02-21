from django.forms import ModelForm
from .models import Lake

class LakeForm(ModelForm):
    class Meta:
        model = Lake
        fields = ['name']