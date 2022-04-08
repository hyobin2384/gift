from django.forms import ModelForm
from django import forms

from mainapp.models import Main


class MainCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable text-left',
                                                           'style':'height: auto'}))


    class Meta:
        model = Main
        fields = ['image', 'content']
