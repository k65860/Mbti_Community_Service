from django import forms
from .models import Write

class WriteForm(forms.ModelForm):
    class Meta:
        model = Write #여기가 위에서 설명한 model
        fields = '__all__'
