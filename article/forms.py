from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):


    image = forms.FileField(required=False)
    class Meta:
        model = Article
        fields = ['title', 'body','image']

