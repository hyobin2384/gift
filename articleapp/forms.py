from django.forms import ModelForm
from django import forms

from articleapp.models import Article


class ArticleCreationForm(ModelForm):

    class Meta:
        model = Article
        fields = ['image']