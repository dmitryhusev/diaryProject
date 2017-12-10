from django import forms
from .models import Tracker

class AssignForm(forms.ModelForm):


    assignee = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Tracker
        fields = '__all__'
